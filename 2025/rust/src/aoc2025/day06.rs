use rdcl_aoc_helpers::input::WithReadLines;
use std::fs::File;

pub fn day06(path: &String) {
    let data: Vec<String> = File::open(path).read_lines::<String>(1).collect();

    let rows = data.len();
    let cols = data[0].len();

    let mut partie1: u64 = 0;
    let mut partie2: u64 = 0;

    let mut numbers_part1: Vec<Vec<u64>> = Vec::new();
    let mut ops: Vec<char> = Vec::new();

    for r in 0..rows - 1 {
        let row = data[r].split(" ").collect::<Vec<_>>();
        let mut numbers: Vec<u64> = Vec::new();
        for item in row {
            if item.parse::<u64>().is_ok() {
                let number = item.parse::<u64>().unwrap();
                numbers.push(number);
            }
        }
        numbers_part1.push(numbers.clone());
    }

    let op_row = data[rows - 1].split(" ").collect::<Vec<_>>();
    for item in op_row {
        if item == "*" || item == "+" {
            ops.push(item.chars().next().unwrap());
        }
    }

    for i in 0..ops.len() {
        let mut result: u64 = 0;
        if ops[i] == '*' {
            result = 1;
            for j in 0..rows - 1 {
                result *= numbers_part1[j][i];
            }
            partie1 += result;
        } else {
            for j in 0..rows - 1 {
                result += numbers_part1[j][i];
            }
            partie1 += result;
        }
    }

    println!("Partie 1: {}", partie1);

    let mut true_numbers: Vec<u64> = Vec::new();
    let mut flag = false;

    let mut op: char = ' ';
    for c in 0..cols {
        let mut n: String = String::new();

        if op == ' ' {
            op = data[rows - 1].chars().nth(c).unwrap();
        }

        for r in 0..rows - 1 {
            n.push(data[r].chars().nth(c).unwrap());
        }
        if n.trim().parse::<u64>().is_ok() {
            true_numbers.push(n.trim().parse::<u64>().unwrap());
        } else {
            flag = true;
        }
        if c == cols - 1 || flag {
            if op == '*' {
                partie2 += true_numbers.iter().product::<u64>();
            } else {
                partie2 += true_numbers.iter().sum::<u64>();
            }
            true_numbers = Vec::new();
            op = ' ';
            flag = false;
        }
    }

    println!("Partie 2: {}", partie2);
}
