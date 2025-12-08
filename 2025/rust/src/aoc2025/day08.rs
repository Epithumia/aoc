use rdcl_aoc_helpers::input::WithReadLines;
use std::collections::HashMap;
use std::fs::File;

pub fn day08(path: &String) {
    let input: Vec<String> = File::open(path).read_lines::<String>(1).collect();
    let mut wires = 1000;
    let points: Vec<Point> = input
        .iter()
        .map(|x| {
            let coords: Vec<&str> = x.split(",").collect();
            Point {
                x: coords[0].parse::<i64>().unwrap(),
                y: coords[1].parse::<i64>().unwrap(),
                z: coords[2].parse::<i64>().unwrap(),
            }
        })
        .collect();

    let mut networks: Vec<i64> = (0..points.len() as i64).collect();

    let mut pairs: Vec<(f64, i64, i64)> = Vec::new();

    for i in 0..points.len() - 1 {
        for j in i + 1..points.len() {
            let distance = ((points[i].x - points[j].x).pow(2)
                + (points[i].y - points[j].y).pow(2)
                + (points[i].z - points[j].z).pow(2))
            .isqrt() as f64;
            pairs.push((distance, i as i64, j as i64));
        }
    }
    pairs.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

    for i in 0..pairs.len() {
        let network1 = networks[pairs[i].1 as usize];
        let network2 = networks[pairs[i].2 as usize];
        if network1 != network2 {
            for idx in 0..points.len() {
                if networks[idx] == network2 {
                    networks[idx] = network1;
                }
            }
        }
        wires -= 1;

        if wires == 0 {
            let counts: HashMap<i64, u32> =
                networks.iter().copied().fold(HashMap::new(), |mut acc, x| {
                    acc.entry(x).and_modify(|e| *e += 1).or_insert(1);
                    acc
                });
            let mut sorted_counts: Vec<&u32> = counts.values().clone().collect::<Vec<&u32>>();
            sorted_counts.sort();
            sorted_counts.reverse();
            println!(
                "Partie 1: {:?}",
                sorted_counts[0] * sorted_counts[1] * sorted_counts[2]
            );
        }
        let check: HashMap<i64, u32> =
            networks.iter().copied().fold(HashMap::new(), |mut acc, x| {
                acc.entry(x).and_modify(|e| *e += 1).or_insert(1);
                acc
            });
        if check.len() == 1 {
            println!(
                "Partie 2: {}",
                points[pairs[i].1 as usize].x * points[pairs[i].2 as usize].x
            );
            break;
        }
    }
}

#[derive(Debug)]
pub struct Point {
    x: i64,
    y: i64,
    z: i64,
}
