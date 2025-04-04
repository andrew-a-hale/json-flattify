use serde_json::Value;
use std::fs::File;
use std::io::BufReader;

fn json_to_path_vec(value: &Value) -> Vec<(String, String)> {
    let mut vec = Vec::new();
    build_path_vec(value, &mut vec, String::new());
    vec
}

fn build_path_vec(value: &Value, vec: &mut Vec<(String, String)>, current_path: String) {
    match value {
        Value::Object(obj) => {
            for (key, val) in obj {
                let current_path = if current_path.is_empty() {
                    key.to_string()
                } else {
                    format!("{}.{}", current_path, key)
                };

                build_path_vec(val, vec, current_path);
            }
        }
        Value::Array(arr) => {
            for (index, val) in arr.iter().enumerate() {
                let current_path = if current_path.is_empty() {
                    index.to_string()
                } else {
                    format!("{}.{}", current_path, index)
                };

                build_path_vec(val, vec, current_path.clone());
            }
        }
        _ => {
            vec.push((current_path, value.to_string()));
        }
    }
}

fn main() {
    let file = File::open("src/tests/large-file.json").expect("failed to open file");
    let buf = BufReader::new(file);
    let json_value: Value = serde_json::from_reader(buf).unwrap();

    for _ in 0..10 {
        let _ = json_to_path_vec(&json_value);
    }
}
