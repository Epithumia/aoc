use geo::{Contains, LineString, Point, Polygon};
use rdcl_aoc_helpers::input::WithReadLines;
use std::fs::File;

pub fn day09(path: &String) {
    let input: Vec<String> = File::open(path).read_lines::<String>(1).collect();
    let points: Vec<Point> = input
        .iter()
        .map(|x| {
            let coords: Vec<&str> = x.split(",").collect();
            Point::new(
                coords[0].parse::<f64>().unwrap(),
                coords[1].parse::<f64>().unwrap(),
            )
        })
        .collect();

    let mut best = 0;

    for i in 0..points.len() - 1 {
        for j in i + 1..points.len() {
            let distance: u64 = (((points[i].x() - points[j].x()).abs() + 1.0)
                * ((points[i].y() - points[j].y()).abs() + 1.0))
                as u64;
            if distance > best {
                best = distance;
            }
        }
    }

    println!("Partie 1: {}", best);

    let area: Polygon = Polygon::new(LineString::from(points.clone()), vec![]);

    best = 0;

    for i in 0..points.len() - 1 {
        for j in i + 1..points.len() {
            let distance: u64 = (((points[i].x() - points[j].x()).abs() + 1.0)
                * ((points[i].y() - points[j].y()).abs() + 1.0))
                as u64;
            if distance > best {
                let p1: Point = points[i];
                let p2: Point = Point::new(points[i].x(), points[j].y());
                let p3: Point = points[j];
                let p4: Point = Point::new(points[j].x(), points[i].y());
                let edges: LineString = LineString::from(vec![p1, p2, p3, p4, p1]);
                if area.contains(&edges) {
                    best = distance;
                }
            }
        }
    }

    println!("Partie 2: {}", best);
}
