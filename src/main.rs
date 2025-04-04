use serde_json::Value;
use std::collections::HashMap;
use std::fs::File;
use std::io::BufReader;

fn json_to_path_map(value: &Value) -> HashMap<String, String> {
    let mut map = HashMap::new();
    build_path_map(value, &mut map, "".to_string());
    map
}

fn build_path_map(value: &Value, map: &mut HashMap<String, String>, current_path: String) {
    match value {
        Value::Object(obj) => {
            for (key, val) in obj {
                let new_path = if current_path.is_empty() {
                    key.to_string()
                } else {
                    format!("{}.{}", current_path, key)
                };
                build_path_map(val, map, new_path);
            }
        }
        Value::Array(arr) => {
            for (index, val) in arr.iter().enumerate() {
                let new_path = format!("{}.{}", current_path, index);
                build_path_map(val, map, new_path);
            }
        }
        Value::String(s) => {
            map.insert(current_path, s.to_string());
        }
        Value::Number(n) => {
            map.insert(current_path, n.to_string());
        }
        Value::Bool(b) => {
            map.insert(current_path, b.to_string());
        }
        Value::Null => {
            map.insert(current_path, "null".to_string());
        }
    }
}

fn main() {
    let file = File::open("src/tests/large-file.json").expect("failed to open file");
    let buf = BufReader::new(file);
    let json_value: Value = serde_json::from_reader(buf).unwrap();

    for _ in 0..10 {
        let _ = json_to_path_map(&json_value);
    }
}
