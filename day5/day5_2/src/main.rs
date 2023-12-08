use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;
use roaring::RoaringBitmap;
fn main() {
    let file = File::open("input.txt").expect("Invalid filename");

    let buf = BufReader::new(file);

    let lines: Vec<String> = buf.lines()
        .map(|line| line.expect("Cant parse this line"))
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

    let mut seeds = vec![];
    let mut map_start = false;
    let mut map_name = String::new();
    // let mut v = RoaringBitmap::new();

    let mut visited: HashSet<i64> = HashSet::new();
    let mut d: Vec<i64> = vec![0; 3989661438+1];
    // let mut d: Vec<i64> = vec![0; 100];

    let mn_regex = Regex::new(r"\w+-\w+-\w+ map").unwrap();
    let number_regex = Regex::new(r"\d+").unwrap();
    for line in &lines {
        let line = line.trim();
        let line_nums: Vec<i64> = number_regex
            .find_iter(line)
            .filter_map(|num| num.as_str().parse().ok())
            .collect();

        if line.contains("seeds:") {
            seeds = line_nums.clone();
        } else if mn_regex.is_match(line) {
            map_name = mn_regex.find(line).unwrap().as_str().to_string();
            map_start = true;
            continue;
        }

        if !line.is_empty() && map_start {
            let (dst, src, length) = (line_nums[0], line_nums[1], line_nums[2]);
            let to = src + length;

            let offset = dst - src;

            for i in (0..seeds.len() - 1).step_by(2) {
                let range_start = seeds[i];
                let range_end = seeds[i] + seeds[i + 1];

                for j in range_start..range_end {
                    let seed = j;
                    let mut temp = seed;

                    if d[seed as usize] == 0 {
                        d[seed as usize] = seed;
                    } else {
                        temp = d[seed as usize];
                    }

                    if src <= temp && temp <= to && !visited.contains(&seed) {
                        temp = d[seed as usize] + offset;
                        d[seed as usize] = temp;
                        // v.insert(seed.try_into().unwrap());
                        visited.insert(seed);
                    }
                }
            }
        } else if line.is_empty() {
            visited = HashSet::new();
            // v = RoaringBitmap::new();
            map_start = false;
            map_name.clear();
        }
    }

    let min_val = d.iter().filter(|&&x| x != 0).cloned().min();
    match min_val {
        Some(min_val) => {
            println!("answer is {}", min_val);
        }
        None => {
            println!("Something went wrong");
        }
    }
}
