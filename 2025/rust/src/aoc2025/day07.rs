use rdcl_aoc_helpers::input::WithReadLines;
use std::fs::File;

pub fn day07(path: &String) {
    let mut diagram: Vec<Vec<char>> = File::open(path).read_lines::<String>(1).map(|x| x.chars().collect()).collect();
    let mut potential: Vec<Vec<u64>> = Vec::new();

    for _i in 0..diagram.len() {
        potential.push(vec![0; diagram[0].len()]);
    }

    for i in 0..diagram[0].len() {
        if diagram[0][i] == 'S' {
            diagram[1][i] = '|';
            potential[1][i] = 1; 
        }
    }

    for i in 1..diagram.len() -1 {
        for j in 0..diagram[0].len() {
            if diagram[i][j] == '^'{
                diagram[i][j - 1] = '|';
                potential[i][j - 1] += potential[i - 1][j];
                diagram[i][j + 1] = '|';
                potential[i][j + 1] += potential[i - 1][j];
            }
        }
        for j in 0..diagram[0].len() {
            if diagram[i][j] == '|' && diagram[i + 1][j] == '.'{
                diagram[i + 1][j] = '|';
                potential[i + 1][j] += potential[i][j];
            }
        }
    }

    let mut partie1 = 0;

    for i in 0..diagram.len() - 1 {
        for j in 0..diagram[0].len() {
            if diagram[i+1][j] == '^' && diagram[i][j] == '|' {
                partie1 += 1;
            }
        }
    }

    let partie2:u64 = potential[diagram.len() - 1].iter().sum();

    println!("Partie 1: {}", partie1);
    println!("Partie 2: {}", partie2);
}