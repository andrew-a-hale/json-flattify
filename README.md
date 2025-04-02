# JSON Flattify

Turn ugly JSON into ugly and flat JSON.

Go from:

```json
{"values":[{"a":1,"b":{"a":1}},{"a":1,"b":[{"values":[1,2,3]},{"values":[1,2,3]}]},{"a":1,"b":2},{"a":1,"b":2},{"a":1,"b":2}]}
{"values":[{"a":1},{"a":1,"b":[{"values":[1,2,3]},{"values":[1,2,3]}]},{"a":1,"b":2},{"a":1,"b":2},{"a":1,"b":2}]}
```

To:

```json
[
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
    "values.4.b": 2
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
    "values.4.b": 2
  }
]
```
