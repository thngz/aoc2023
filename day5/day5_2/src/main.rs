use regex::Regex;
use std::collections::HashSet;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::sync::mpsc;
use std::thread;

fn main() {
    let file = File::open("input.txt").expect("Invalid filename");

    let buf = BufReader::new(file);

    let lines: Vec<String> = buf
        .lines()
        .map(|line| line.expect("Cant parse this line"))
        .map(|line| line.trim().to_string())
        .collect();

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
    let mut seeds = vec![];
    let mut map_start = false;
    let mut map_name = String::new();
    let mut maps: Vec<(i64, i64, i64, String)> = Vec::new();

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
            seed_chunks = seeds.clone().chunks(2).map(|chunk| chunk.to_vec()).collect();
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

    for chunk in seed_chunks {
        let maps = maps.clone();
        let tx = tx.clone();
        let seeds = seeds.clone();
        thread::spawn(move || {
            println!("Currently on seed: {:?}", chunk);
            for i in (0..chunk.len() - 1).step_by(2) {
                let range_start = seeds[i];
                let range_end = seeds[i] + seeds[i + 1];
                for j in range_start..range_end {
                    tx.send(get_location(j, &maps)).unwrap();
                }
            }
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
        }
        None => {
            println!("????");
        }
    }
}
