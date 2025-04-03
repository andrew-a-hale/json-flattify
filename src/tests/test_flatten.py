import os

import pytest

from flatten import flatten_json, flatten_jsonl

PATH = os.path.dirname(__file__)


@pytest.mark.parametrize("file", ["tests/lines-simple.jsonl"])
def test_flatten_jsonl(file: str):
    test = flatten_jsonl(file)
    expected = [{"a": 1, "b": 2}, {"a": 1, "b": 2}]
    assert test == expected


@pytest.mark.parametrize("file", ["tests/lines-complex.jsonl"])
def test_flatten_jsonl_2(file: str):
    test = flatten_jsonl(file)
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
def test_flatten(file: str):
    test = flatten_json(file)
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
def test_flatten_2(file: str):
    test = flatten_json(file)
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
def test_flatten_3(file: str):
    test = flatten_json(file)
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


@pytest.mark.parametrize("file", ["tests/array.json"])
def test_flatten_array_simple(file: str):
    test = flatten_json(file)
    expected = [{"0": 1, "1": 2, "2": 3}]
    assert test == expected


@pytest.mark.parametrize("file", ["tests/array-objs.json"])
def test_flatten_array(file: str):
    test = flatten_json(file)
    expected = [{"0.a": 1, "1.a": 1, "2.a": 1, "3.a": 1}]
    assert test == expected
