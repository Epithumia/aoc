use rdcl_aoc_helpers::input::WithReadLines;
use std::fs::File;

fn greedy_number(row: &Vec<u8>, n: u8) -> u64 {
    let mut number: u64 = 0;
    let mut window = row.to_vec();

    for i in 0..n {
        let p = n - i - 1;
        if p > 0 {
            let len = window.len();
            let v = u64::from(*window[..(len - (p as usize))].iter().max().unwrap());
            number += v * (10_u64.pow(p as u32));
            let x = window.iter().position(|&x| u64::from(x) == v).unwrap() + 1;
            window = window[x..].to_vec();
        } else {
            let v: u64 = u64::from(*window.iter().max().unwrap());
            number += v * (10_u64.pow(p as u32));
        }
    }

    return number;
}

pub fn day03(path: &String) {
    let input: Vec<Vec<u8>> = File::open(path)
        .read_lines::<String>(1)
        .into_iter()
        .map(|x| {
            x.chars()
                .map(|x| x.to_string().parse::<u8>().unwrap())
                .collect()
        })
        .collect();

    let mut part1 = 0;
    let mut part2 = 0;

    for row in input {
        part1 += greedy_number(&row, 2);
        part2 += greedy_number(&row, 12);
    }

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
