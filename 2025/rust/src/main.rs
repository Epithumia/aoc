mod aoc2025;

use crate::aoc2025::day01::day01;
use crate::aoc2025::day02::day02;

use rdcl_aoc_helpers::args::get_args;

fn main() {
    let args = get_args(&["<day>", "<inputs path>"], 1);
    let day: u8 = args[1].parse::<u8>().unwrap();
    let path = &args[2];

    match day {
        1 => day01(&path.to_string()),
        2 => day02(&path.to_string()),
        /*
        3 => day3(&path.to_string()),
        4 => day4(&path.to_string()),
        5 => day5(&path.to_string()),
        6 => day6(&path.to_string()),
        7 => day7(&path.to_string()),
        8 => day8(&path.to_string()),
        9 => day9(&path.to_string()),
        10 => day10(&path.to_string()),
        11 => day11(&path.to_string()),
        12 => day12(&path.to_string()),
        */
        _ => println!("Nothing to do"),
        // Jour non codé
    }
}
