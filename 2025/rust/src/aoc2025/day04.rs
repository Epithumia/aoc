use rdcl_aoc_helpers::input::WithReadLines;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::File;

fn accessible(map: &mut HashMap<(i32, i32), char>, coord: (i32, i32)) -> bool {
    if *map.entry(coord).or_insert('.') == '.' {
        return false;
    }
    let mut neighbors = 0;
    for (i, j) in [
        (coord.0 - 1, coord.1),
        (coord.0 + 1, coord.1),
        (coord.0, coord.1 - 1),
        (coord.0, coord.1 + 1),
        (coord.0 - 1, coord.1 - 1),
        (coord.0 - 1, coord.1 + 1),
        (coord.0 + 1, coord.1 - 1),
        (coord.0 + 1, coord.1 + 1),
    ] {
        if *map.entry((i, j)).or_insert('.') == '@' {
            neighbors += 1;
        }
    }
    if neighbors >= 4 {
        return false;
    }
    return true;
}

pub fn day04(path: &String) {
    let input: Vec<Vec<char>> = File::open(path)
        .read_lines::<String>(1)
        .into_iter()
        .map(|x| x.chars().collect())
        .collect();

    let mut map: HashMap<(i32, i32), char> = HashMap::new();

    let rows = input.len();
    let cols = input[0].len();

    for i in 0..rows {
        for j in 0..cols {
            map.insert((i as i32, j as i32), input[i][j]);
        }
    }

    let mut part1 = 0;
    let mut part2 = 0;

    for i in 0..rows {
        for j in 0..cols {
            if accessible(&mut map, (i as i32, j as i32)) {
                part1 += 1;
            }
        }
    }

    println!("Part 1: {}", part1);

    let mut updated = true;
    let mut seen: HashSet<(i32, i32)> = HashSet::new();
    while updated {
        updated = false;
        for i in 0..rows {
            for j in 0..cols {
                if !seen.contains(&(i as i32, j as i32))
                    && accessible(&mut map, (i as i32, j as i32))
                {
                    part2 += 1;
                    seen.insert((i as i32, j as i32));
                    updated = true;
                }
            }
        }
        for s in &seen {
            map.entry(*s).and_modify(|e| *e = '.');
        }
    }

    println!("Part 2: {}", part2);
}
