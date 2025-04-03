import os
import json

PATH = os.path.dirname(__file__)


def _flatten_list(obj: list, path: str = "", tuples: list = []) -> list:
    for i, v in enumerate(obj):
        new_path = ".".join(x for x in [path, str(i)] if x)
        if isinstance(v, dict):
            _flatten_obj(v, new_path, tuples)
        elif isinstance(v, list):
            _flatten_list(v, new_path, tuples)
        else:
            tuples.append((new_path, v))

    return tuples


def _flatten_obj(obj: dict, path: str = "", tuples: list = []) -> list:
    for k, v in obj.items():
        new_path = ".".join(x for x in [path, k] if x)
        if isinstance(v, dict):
            _flatten_obj(v, new_path, tuples)
        elif isinstance(v, list):
            _flatten_list(v, new_path, tuples)
        else:
            tuples.append((new_path, v))

    return tuples


def flatten_json(file: str) -> list:
    with open(os.path.join(PATH, file)) as f:
        tuples = []
        obj = json.load(f)
        if isinstance(obj, dict):
            tuples.extend(_flatten_obj(obj, "", []))
        elif isinstance(obj, list):
            tuples.extend(_flatten_list(obj, "", []))
        else:
            tuples.append(("value", obj))

    return [{x: y for x, y in tuples}]


def flatten_jsonl(file: str) -> list:
    lines = []
    with open(os.path.join(PATH, file)) as f:
        for line in f:
            obj = json.loads(line)
            lines.append({x: y for x, y in _flatten_obj(obj, "", [])})

    return lines


if __name__ == "__main__":
    print(flatten_jsonl("tests/lines-complex.jsonl"))
