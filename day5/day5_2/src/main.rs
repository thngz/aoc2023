use regex::Regex;
use std::collections::HashSet;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::sync::mpsc;
use std::thread;
use threadpool::ThreadPool;
fn main() {
    let file = File::open("input.txt").expect("Invalid filename");

    let buf = BufReader::new(file);

    let lines: Vec<String> = buf
        .lines()
        .map(|line| line.expect("Cant parse this line"))
        .map(|line| line.trim().to_string())
        .collect();
    //
    // let lines = vec![
    //     "seeds: 79 14 55 13",
    //     "         ",
    //     "seed-to-soil map:",
    //     "50 98 2",
    //     "52 50 48",
    //     "        ",
    //     "soil-to-fertilizer map:",
    //     "0 15 37",
    //     "37 52 2",
    //     "39 0 15",
    //     "        ",
    //     "fertilizer-to-water map:",
    //     "49 53 8",
    //     "0 11 42",
    //     "42 0 7",
    //     "57 7 4",
    //     "       ",
    //     "water-to-light map:",
    //     "88 18 7",
    //     "18 25 70",
    //     "         ",
    //     "light-to-temperature map:",
    //     "45 77 23",
    //     "81 45 19",
    //     "68 64 13",
    //     "         ",
    //     "temperature-to-humidity map:",
    //     "0 69 1",
    //     "1 0 69",
    //     "       ",
    //     "humidity-to-location map:",
    //     "60 56 37",
    //     "56 93 4",
    // ];
    // 1445869986 - TOO HIGH!
    // 650599855 - TOO HIGH
    // 2107309188
    // 1240036 - CLOSE
    let mut seeds = vec![];
    let mut map_start = false;
    let mut map_name = String::new();
    let mut maps: Vec<(i64, i64, i64, String)> = Vec::new();

    let workers = 5;
    let pool = ThreadPool::new(workers);

    let chunk_size = 2;
    let (tx, rx) = mpsc::channel();

    let mut locations: Vec<i64> = vec![];

    let mn_regex = Regex::new(r"\w+-\w+-\w+ map").unwrap();
    let number_regex = Regex::new(r"\d+").unwrap();
    let mut seed_chunks: Vec<Vec<i64>> = vec![];
    for line in &lines {
        let line = line.trim();
        let line_nums: Vec<i64> = number_regex
            .find_iter(line)
            .filter_map(|num| num.as_str().parse().ok())
            .collect();

        if line.contains("seeds:") {
            seeds = line_nums.clone();
            seed_chunks = seeds
                .clone()
                .chunks(chunk_size)
                .map(|chunk| chunk.to_vec())
                .collect();
        } else if mn_regex.is_match(line) {
            map_name = mn_regex.find(line).unwrap().as_str().to_string();
            map_start = true;
            continue;
        }

        if !line.is_empty() && map_start {
            maps.push((line_nums[0], line_nums[1], line_nums[2], map_name.clone()));
        } else if line.is_empty() {
            map_start = false;
            map_name.clear();
        }
    }

    fn get_location(mut seed: i64, maps: &Vec<(i64, i64, i64, String)>) -> i64 {
        let mut visited_mappings: HashSet<String> = HashSet::new();

        for (dst, src, length, map_name) in maps {
            let to = src + length;
            let offset = dst - src;

            if src <= &seed && &seed <= &to && !visited_mappings.contains(map_name) {
                seed += offset;
                visited_mappings.insert(map_name.to_string());
            }
        }

        seed
    }

    fn chunkify(start: i64, end: i64, chunk_size: i64) -> Vec<Vec<i64>> {
        let mut subchunks = Vec::new();
        let mut current_start = start;

        while current_start <= end {
            let current_end = (current_start + chunk_size - 1).min(end);
            subchunks.push((current_start..=current_end).collect());
            current_start = current_end + 1;
        }

        subchunks
    }
    println!("All chunks: {:?}", seed_chunks);
    for chunk in seed_chunks.clone() {
        let s = chunk[0];
        let e = chunk[1];

        let maps = maps.clone();
        let tx = tx.clone();
        let start = s.max(e);
        let end = s.max(e) + s.min(e) - 1;
        let subchunk_size = (end - start + 1) / workers as i64;
        pool.execute(move || {
            let mut ls: Vec<i64> = vec![];

            println!(
                "Processing chunk {:?}, chunk size: {}",
                chunk,
                subchunk_size
            );
            for subchunk in chunkify(start, end, subchunk_size) {
                // println!("Currently on subchunk: {:?}", subchunk);
                let range_start = subchunk[0];
                let range_end = subchunk.last().unwrap();
                for j in range_start..=*range_end {
                    // println!("{} {} {}", range_start, range_end, j);
                    ls.push(get_location(j, &maps));
                }
            }
            let m = ls.iter().min().unwrap();
            println!("Finished processing chunk {:?}", chunk,);
            tx.send(m.clone()).unwrap();
        });
    }

    drop(tx);
    for received in rx {
        locations.push(received);
    }
    println!("Finding minimum");
    let minimum = locations.iter().min();
    match minimum {
        Some(minimum) => {
            println!("answer is {}", minimum);
            // println!("locations is {:?}", locations);
        }
        None => {
            println!("????");
        }
    }
}
