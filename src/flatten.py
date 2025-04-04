import os
import json

PATH = os.path.dirname(__file__)


def _flatten(obj: dict, path: str = "", tuples: list = []) -> list:
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = f"{path}.{k}" if path else k
            _flatten(v, new_path, tuples)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_path = f"{path}.{i}" if path else str(i)
            _flatten(v, new_path, tuples)
    else:
        tuples.append((path, obj))

    return tuples


def flatten_json(file: str) -> list:
    with open(os.path.join(PATH, file)) as f:
        tuples = []
        obj = json.loads(f.read())
        tuples.extend(_flatten(obj, "", []))

    return [{x: y for x, y in tuples}]


def flatten_jsonl(file: str) -> list:
    lines = []
    with open(os.path.join(PATH, file)) as f:
        for line in f:
            obj = json.loads(line)
            lines.append({x: y for x, y in _flatten(obj, "", [])})

    return lines


if __name__ == "__main__":
    flatten_json("tests/large-file.json")
