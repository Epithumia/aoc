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

    let mut pre_calc_surfaces: Vec<(u64, Point, Point)> = Vec::new();

    for i in 0..points.len() - 1 {
        for j in i + 1..points.len() {
            let distance: u64 = (((points[i].x() - points[j].x()).abs() + 1.0)
                * ((points[i].y() - points[j].y()).abs() + 1.0))
                as u64;
            pre_calc_surfaces.push((distance, points[i], points[j]));
        }
    }

    pre_calc_surfaces.sort_by(|a, b| b.0.cmp(&a.0));

    println!("Partie 1: {}", pre_calc_surfaces[0].0);

    let area: Polygon = Polygon::new(LineString::from(points.clone()), vec![]);

    let mut best = 0;

    for p in pre_calc_surfaces {
        if p.0 > best {
            let p1 = p.1;
            let p3 = p.2;
            let p2 = Point::new(p1.x(), p3.y());
            let p4 = Point::new(p3.x(), p1.y());
            let edges: LineString = LineString::from(vec![p1, p2, p3, p4, p1]);
            if area.contains(&edges) {
                best = p.0;
                break;
            }
        }
    }

    println!("Partie 2: {}", best);
}
