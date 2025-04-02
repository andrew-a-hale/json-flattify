import os

import pytest

from parse import parse_json, parse_jsonl

PATH = os.path.dirname(__file__)


@pytest.mark.parametrize("file", ["tests/lines-simple.jsonl"])
def test_parse_jsonl(file: str):
    test = parse_jsonl(file)
    expected = [{"a": 1, "b": 2}, {"a": 1, "b": 2}]
    assert test == expected


@pytest.mark.parametrize("file", ["tests/lines-complex.jsonl"])
def test_parse_jsonl_2(file: str):
    test = parse_jsonl(file)
    expected = [
        {
            "values.0.a": 1,
            "values.0.b.a": 1,
            "values.1.a": 1,
            "values.1.b.0.values.0": 1,
            "values.1.b.0.values.1": 2,
            "values.1.b.0.values.2": 3,
            "values.1.b.1.values.0": 1,
            "values.1.b.1.values.1": 2,
            "values.1.b.1.values.2": 3,
            "values.2.a": 1,
            "values.2.b": 2,
            "values.3.a": 1,
            "values.3.b": 2,
            "values.4.a": 1,
            "values.4.b": 2,
        },
        {
            "values.0.a": 1,
            "values.1.a": 1,
            "values.1.b.0.values.0": 1,
            "values.1.b.0.values.1": 2,
            "values.1.b.0.values.2": 3,
            "values.1.b.1.values.0": 1,
            "values.1.b.1.values.1": 2,
            "values.1.b.1.values.2": 3,
            "values.2.a": 1,
            "values.2.b": 2,
            "values.3.a": 1,
            "values.3.b": 2,
            "values.4.a": 1,
            "values.4.b": 2,
        },
    ]
    assert test == expected


@pytest.mark.parametrize("file", ["tests/simple.json"])
def test_parse(file: str):
    test = parse_json(file)
    expected = [
        {
            "values.0.a": 1,
            "values.0.b": 2,
            "values.1.a": 1,
            "values.1.b": 2,
            "values.2.a": 1,
            "values.2.b": 2,
            "values.3.a": 1,
            "values.3.b": 2,
            "values.4.a": 1,
            "values.4.b": 2,
        }
    ]
    assert test == expected


@pytest.mark.parametrize("file", ["tests/normal.json"])
def test_parse_2(file: str):
    test = parse_json(file)
    expected = [
        {
            "values.0.a": 1,
            "values.0.b.a": 1,
            "values.1.a": 1,
            "values.1.b": 2,
            "values.2.a": 1,
            "values.2.b": 2,
            "values.3.a": 1,
            "values.3.b": 2,
            "values.4.a": 1,
            "values.4.b": 2,
        }
    ]
    assert test == expected


@pytest.mark.parametrize("file", ["tests/complex.json"])
def test_parse_3(file: str):
    test = parse_json(file)
    expected = [
        {
            "values.0.a": 1,
            "values.0.b.a": 1,
            "values.1.a": 1,
            "values.1.b.0.values.0": 1,
            "values.1.b.0.values.1": 2,
            "values.1.b.0.values.2": 3,
            "values.1.b.1.values.0": 1,
            "values.1.b.1.values.1": 2,
            "values.1.b.1.values.2": 3,
            "values.2.a": 1,
            "values.2.b": 2,
            "values.3.a": 1,
            "values.3.b": 2,
            "values.4.a": 1,
            "values.4.b": 2,
        }
    ]
    assert test == expected
