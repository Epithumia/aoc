use good_lp::variable::ProblemVariables;
use good_lp::{Expression, SolverModel, Variable, default_solver, variable};
use rdcl_aoc_helpers::input::WithReadLines;
use std::cmp::min;
use std::fmt::Debug;
use std::fs::File;

struct State {
    size: u8,
    current: u32,
}

impl State {
    fn new(size: u8) -> State {
        State {
            size: size,
            current: 0,
        }
    }
}

impl Iterator for State {
    type Item = Vec<u8>;

    fn next(&mut self) -> Option<Self::Item> {
        if self.size == 0 || self.current >= 2_u32.pow(self.size as u32) {
            None
        } else {
            let seq = (0..self.size)
                .map(|x| ((self.current & (1 << x)) >> x) as u8)
                .collect();
            self.current += 1;
            Some(seq)
        }
    }
}

struct Machine {
    target_state: Vec<u8>,
    target_joltage: Vec<u16>,
    buttons: Vec<Vec<u8>>,
    state: Vec<u8>,
    joltage_buttons: ProblemVariables,
}

impl Machine {
    fn new(data: String) -> Machine {
        let parts: Vec<Vec<char>> = data.split(" ").map(|x| x.chars().collect()).collect();
        let target: Vec<u8> = parts[0][1..parts[0].len() - 1]
            .iter()
            .map(|x| if *x == '.' { 0 } else { 1 })
            .collect();
        Machine {
            target_state: target.clone(),
            target_joltage: parts[parts.len() - 1][1..parts[parts.len() - 1].len() - 1]
                .into_iter()
                .collect::<String>()
                .split(',')
                .map(|x| x.parse::<u16>().unwrap())
                .collect(),
            buttons: parts[1..parts.len() - 1]
                .iter()
                .map(|x| {
                    x[1..x.len() - 1]
                        .into_iter()
                        .collect::<String>()
                        .split(',')
                        .map(|x| x.to_string().parse::<u8>().unwrap())
                        .collect()
                })
                .collect(),
            state: vec![0; target.len()],
            joltage_buttons: ProblemVariables::new(),
        }
    }

    fn press(&mut self, button: Vec<u8>) {
        for b in button {
            self.state[b as usize] = (self.state[b as usize] + 1) % 2;
        }
    }

    fn solve_part1(&mut self) -> u32 {
        let mut best: u32 = 10000000;
        for state in State::new(self.buttons.len() as u8) {
            for bit in 0..state.len() {
                if state[bit] == 1 {
                    self.press(self.buttons[bit].clone());
                }
            }
            if self.state == self.target_state {
                best = min(best, state.into_iter().map(|x| x as u32).sum());
            }
            self.reset();
        }
        best
    }

    fn reset(&mut self) {
        self.state = vec![0; self.target_state.len()];
    }

    fn solve_part2(&mut self) -> u32 {
        let vars = vec![variable().integer().min(0).max(400); self.buttons.len()];
        let b: Vec<Variable> = self.joltage_buttons.add_all(vars);
        let objective: Expression = b.iter().sum();
        let mut model = self
            .joltage_buttons
            .clone()
            .minimise(&objective)
            .using(default_solver);

        for i in 0..self.target_state.len() as u8 {
            let switches: Vec<u8> = self
                .buttons
                .iter()
                .map(|button| if button.contains(&i) { 1 } else { 0 })
                .collect();
            let mut con: Expression = Expression::from_other_affine(0);
            for k in 0..self.buttons.len() {
                con.add_mul(switches[k], b[k]);
            }
            model = model.with(con.eq(self.target_joltage[i as usize]));
        }
        model.set_parameter("log", "0");
        let solution = model.solve().unwrap();
        objective.eval_with(&solution) as u32
    }
}

impl Debug for Machine {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("Machine")
            .field("target_state", &self.target_state)
            .field("target_joltage", &self.target_joltage)
            .field("buttons", &self.buttons)
            .field("state", &self.state)
            .finish()
    }
}

pub fn day10(path: &String) {
    let input: Vec<String> = File::open(path).read_lines::<String>(1).collect();
    let mut machines: Vec<Machine> = Vec::new();
    for line in input {
        machines.push(Machine::new(line));
    }

    let mut partie1 = 0;
    let mut partie2 = 0;
    for mut machine in machines {
        partie1 += machine.solve_part1();
        partie2 += machine.solve_part2();
    }

    println!("Partie 1: {}", partie1);
    println!("Partie 2: {}", partie2);
}
