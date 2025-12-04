use rdcl_aoc_helpers::input::WithReadLines;
use std::cmp::max;
use std::fs::File;

#[derive(Debug)]
struct IDRange {
    low: u64,
    high: u64,
    invalid_id: u64,
    seen: Vec<u64>,
}

impl IDRange {
    fn new(low: u64, high: u64) -> IDRange {
        IDRange {
            low: low,
            high: high,
            invalid_id: 0,
            seen: Vec::new(),
        }
    }
}

impl Iterator for IDRange {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let nb_digits_low = max(self.low.to_string().len(), 2);
        let nb_digits_high = self.high.to_string().len();

        for nb_digits in nb_digits_low..=nb_digits_high {
            match nb_digits {
                2 => {
                    for i in (11..100).step_by(11) {
                        if i >= self.low && i <= self.high && !self.seen.contains(&i) {
                            self.invalid_id = i;
                            self.seen.push(i);
                            return Some(i);
                        }
                    }
                }
                3 => {
                    for i in (111..1000).step_by(111) {
                        if i >= self.low && i <= self.high && !self.seen.contains(&i) {
                            self.invalid_id = i;
                            self.seen.push(i);
                            return Some(i);
                        }
                    }
                }
                4 => {
                    for i in (1111..10000).step_by(1111) {
                        if i >= self.low && i <= self.high && !self.seen.contains(&i) {
                            self.invalid_id = i;
                            self.seen.push(i);
                            return Some(i);
                        }
                    }
                    for i in 10..100 {
                        let n = i * 100 + i;
                        if n >= self.low && n <= self.high && !self.seen.contains(&n) {
                            self.invalid_id = n;
                            self.seen.push(n);
                            return Some(n);
                        }
                    }
                }
                5 => {
                    for i in (11111..100000).step_by(11111) {
                        if i >= self.low && i <= self.high && !self.seen.contains(&i) {
                            self.invalid_id = i;
                            self.seen.push(i);
                            return Some(i);
                        }
                    }
                }
                6 => {
                    for i in 10..100 {
                        let n = i * 10000 + i * 100 + i;
                        if n >= self.low && n <= self.high && !self.seen.contains(&n) {
                            self.invalid_id = n;
                            self.seen.push(n);
                            return Some(n);
                        }
                    }
                    for i in 100..1000 {
                        let n = i * 1000 + i;
                        if n >= self.low && n <= self.high && !self.seen.contains(&n) {
                            self.invalid_id = n;
                            self.seen.push(n);
                            return Some(n);
                        }
                    }
                }
                7 => {
                    for i in (1111111..10000000).step_by(1111111) {
                        if i >= self.low && i <= self.high && !self.seen.contains(&i) {
                            self.invalid_id = i;
                            self.seen.push(i);
                            return Some(i);
                        }
                    }
                }
                8 => {
                    for i in 1000..10000 {
                        let n = i * 10000 + i;
                        if n >= self.low && n <= self.high && !self.seen.contains(&n) {
                            self.invalid_id = n;
                            self.seen.push(n);
                            return Some(n);
                        }
                    }
                }
                9 => {
                    for i in 100..1000 {
                        let n = i * 1000000 + i * 1000 + i;
                        if n >= self.low && n <= self.high && !self.seen.contains(&n) {
                            self.invalid_id = n;
                            self.seen.push(n);
                            return Some(n);
                        }
                    }
                }
                10 => {
                    for i in 10..100 {
                        let n = i * 100000000 + i * 1000000 + i * 10000 + i * 100 + i;
                        if n >= self.low && n <= self.high && !self.seen.contains(&n) {
                            self.invalid_id = n;
                            self.seen.push(n);
                            return Some(n);
                        }
                    }
                    for i in 10000..100000 {
                        let n = i * 100000 + i;
                        if n >= self.low && n <= self.high && !self.seen.contains(&n) {
                            self.invalid_id = n;
                            self.seen.push(n);
                            return Some(n);
                        }
                    }
                }
                _ => return None,
            }
        }
        return None;
    }
}

fn simple_invalid_id(val: u64) -> bool {
    let id_str = val.to_string();
    if id_str.len() % 2 == 1 {
        return false;
    }
    // check if the first half of the string is equal to the second half
    if id_str[0..id_str.len() / 2] == id_str[id_str.len() / 2..] {
        return true;
    }
    false
}

pub fn day02(path: &String) {
    let input: String = File::open(path).read_lines::<String>(1).next().unwrap();

    let mut data: Vec<IDRange> = input
        .split(",")
        .map(|s| {
            s.split_once('-')
                .map(|(a, b)| IDRange::new(a.parse::<u64>().unwrap(), b.parse::<u64>().unwrap()))
                .unwrap()
        })
        .collect();

    let mut score1 = 0;
    let mut score2 = 0;

    for r in &mut data {
        r.for_each(|i| {
            score2 += i;
            if simple_invalid_id(i) {
                score1 += i;
            }
        })
    }

    println!("Part 1: {}", score1);
    println!("Part 2: {}", score2);
}
