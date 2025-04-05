use serde_json::Value;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn flatten_json(file: File) -> HashMap<String, Value> {
    let buf = BufReader::new(file);
    let json_value: Value = serde_json::from_reader(buf).unwrap();
    let mut map: HashMap<String, Value> = HashMap::new();
    _flatten(&json_value, &mut map, String::new());
    map
}

fn flatten_jsonl(file: File) -> Vec<HashMap<String, Value>> {
    let mut maps: Vec<HashMap<String, Value>> = vec![];
    BufReader::new(file).lines().for_each(|line| match line {
        Ok(line) => {
            let json_value: Value = serde_json::from_str(line.as_str()).unwrap();
            let mut map: HashMap<String, Value> = HashMap::new();
            _flatten(&json_value, &mut map, String::new());
            maps.push(map);
        }
        Err(_) => eprintln!("failed to read line"),
    });
    maps
}

fn _flatten(value: &Value, map: &mut HashMap<String, Value>, current_path: String) {
    match value {
        Value::Object(obj) => obj.iter().for_each(|(k, v)| {
            let current_path = if current_path.is_empty() {
                k.to_string()
            } else {
                format!("{}.{}", current_path, k)
            };
            _flatten(v, map, current_path);
        }),
        Value::Array(arr) => arr.iter().enumerate().for_each(|(i, v)| {
            let current_path = if current_path.is_empty() {
                i.to_string()
            } else {
                format!("{}.{}", current_path, i)
            };
            _flatten(v, map, current_path.clone());
        }),
        v => {
            map.insert(current_path, v.clone());
        }
    }
}

fn main() {
    let file = File::open("src/tests/complex.json").expect("failed to open file");
    println!("{:?}", flatten_json(file));

    let file = File::open("src/tests/lines-complex.jsonl").expect("failed to open file");
    println!("{:?}", flatten_jsonl(file));
}
