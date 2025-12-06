use rdcl_aoc_helpers::input::WithReadLines;
use std::fs::File;

pub fn day05(path: &String) {
    let data: Vec<String> = File::open(path).read_lines::<String>(1).collect();
    let mut intervals: Vec<(u64, u64)> = Vec::new();
    let mut merged_intervals: Vec<(u64, u64)> = Vec::new();
    let mut ids: Vec<u64> = Vec::new();

    for line in data {
        if line.contains('-') {
            let interval: Vec<u64> = line.split('-').map(|x| x.parse::<u64>().unwrap()).collect();
            intervals.push((interval[0], interval[1]));
        } else if line.len() > 0 {
            ids.push(line.parse::<u64>().unwrap());
        }
    }

    intervals.sort_by(|a, b| a.0.cmp(&b.0));
    merged_intervals.push(intervals[0]);

    for interval in intervals {
        let last = merged_intervals.pop().unwrap();
        if last.0 <= interval.0 && interval.0 <= last.1 {
            if last.1 < interval.1 {
                merged_intervals.push((last.0, interval.1));
            } else {
                merged_intervals.push(last);
            }
        } else {
            merged_intervals.push(last);
            merged_intervals.push(interval);
        }
    }

    let partie1: u64 = ids
        .iter()
        .filter(|x| merged_intervals.iter().any(|y| y.0 <= **x && y.1 >= **x))
        .count() as u64;
    println!("Partie 1: {}", partie1);
    let partie2: u64 = merged_intervals.iter().map(|x| x.1 - x.0 + 1).sum();

    println!("Partie 2: {}", partie2);
}
