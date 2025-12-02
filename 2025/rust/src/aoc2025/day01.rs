use rdcl_aoc_helpers::input::WithReadLines;
use std::fs::File;

pub fn day01(path: &String) {
    let mut p1: i32 = 0;
    let mut p2: i32 = 0;
    let mut dial: i32 = 50;

    let data: Vec<String> = File::open(path).read_lines::<String>(1).collect();

    for row in data {
        let value: i32 = row
            .chars()
            .filter(|c| c.is_digit(10))
            .collect::<String>()
            .parse::<i32>()
            .unwrap();
        let direction: String = row.chars().filter(|c| !c.is_digit(10)).collect();

        if direction == "R" {
            if dial + value > 100 {
                p2 += (dial + value).checked_div(100).unwrap();
                if (dial + value) % 100 == 0 {
                    p2 -= 1;
                }
            }
            dial = (dial + value) % 100;
        } else {
            if dial - value < 0 {
                p2 += (dial - value).abs().checked_div(100).unwrap() + 1;
                if (dial - value).rem_euclid(100) == 0 || dial == 0 {
                    p2 -= 1;
                }
            }
            dial = (dial - value).rem_euclid(100);
        }

        if dial == 0 {
            p1 += 1;
        }
    }

    println!("Partie 1 : {:?}", p1);
    println!("Partie 2 : {:?}", p1 + p2);
}
