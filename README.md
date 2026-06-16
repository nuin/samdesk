# samdesk — Advent of Code 2024

Personal solutions to [Advent of Code 2024](https://adventofcode.com/2024) puzzles.

## Day 2 — Red-Nosed Reports (Part 1)

File: [`safe_unsafe.py`](./safe_unsafe.py)

Each line of `input.txt` is a *report*: a whitespace-separated list of integer
levels. The puzzle asks how many reports are *safe* under these rules:

1. The levels are either **all increasing** or **all decreasing**.
2. Any two adjacent levels differ by **at least 1** and **at most 3**.

### Run

```shell
python3 safe_unsafe.py
```

### Expected output

```
Safe: 218
```

## Repo layout

| Path             | Purpose                                          |
| ---------------- | ------------------------------------------------ |
| `safe_unsafe.py` | Day 2 Part 1 solver                              |
| `input.txt`      | Puzzle input — one report per line               |

## Requirements

- Python 3.9+ (uses `list[int]` PEP 585 generics in type hints)
- No third-party dependencies
