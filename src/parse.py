import os
import json

PATH = os.path.dirname(__file__)


def _parse_list(obj: list, path: str = "", tuples: list = []) -> list:
    for i, v in enumerate(obj):
        new_path = ".".join(x for x in [path, str(i)] if x)
        if isinstance(v, dict):
            _parse_obj(v, new_path, tuples)
        elif isinstance(v, list):
            _parse_list(v, new_path, tuples)
        else:
            tuples.append((new_path, v))

    return tuples


def _parse_obj(obj: dict, path: str = "", tuples: list = []) -> list:
    for k, v in obj.items():
        new_path = ".".join(x for x in [path, k] if x)
        if isinstance(v, dict):
            _parse_obj(v, new_path, tuples)
        elif isinstance(v, list):
            _parse_list(v, new_path, tuples)
        else:
            tuples.append((new_path, v))

    return tuples


def parse_json(file: str) -> list:
    with open(os.path.join(PATH, file)) as f:
        lines = json.load(f)
        tuples = _parse_obj(lines, "", [])

    return [{x: y for x, y in tuples}]


def parse_jsonl(file: str) -> list:
    lines = []
    with open(os.path.join(PATH, file)) as f:
        for line in f:
            lines.append({x: y for x, y in _parse_obj(json.loads(line), "", [])})

    return lines


if __name__ == "__main__":
    df = parse_jsonl("tests/lines-complex.jsonl")
    print(df)
