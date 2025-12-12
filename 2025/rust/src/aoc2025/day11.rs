use rdcl_aoc_helpers::input::WithReadLines;
use std::fs::File;
use std::collections::HashMap;


fn count_paths(n: u32, edges: &Vec<Vec<u32>>, source: u32, destination: u32) -> u64 {
    
}

pub fn day11(path: &String) {
    let input: Vec<String> = File::open(path).read_lines::<String>(1).collect();

    let mut nodes:HashMap<String, Vec<String>> = HashMap::new();
    let mut id_nodes:HashMap<String, u32> = HashMap::new();
    let mut id = 1;

    for row in &input {
        let s1 = row.split_once(": ").unwrap();
        let start = s1.0;
        let s2 = s1.1.split(" ").map(|x| x.to_string()).collect::<Vec<String>>();
        nodes.insert(start.to_string(), s2);
    }
    for key in nodes.keys() {
        id_nodes.insert(key.to_string(), id);
        id += 1;
    }
    id_nodes.insert( "out".to_string(), id);

    let mut graph:Vec<Vec<u32>> = Vec::new();

    for item in &nodes {
        for node in item.1 {
            graph.push(vec![id_nodes.get(item.0).unwrap().clone(), id_nodes.get(node).unwrap().clone()]);
        }
    }

    println!("{:?}", graph);
    println!("Partie 1: {}", 0);
    println!("Partie 2: {}", 0);
}