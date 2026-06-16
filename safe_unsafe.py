"""Advent of Code 2024 — Day 2: Red-Nosed Reports (Part 1).

Reads reactor reports from ``input.txt`` (one report per line, whitespace-
separated integer levels) and counts how many are considered *safe*.

A report is **safe** when:

1. Its levels are strictly monotonic (all increasing or all decreasing), and
2. Each pair of adjacent levels differs by at least 1 and at most 3.

Expected answer for the supplied puzzle input: ``218``.

:Usage:

.. code-block:: shell

    python safe_unsafe.py
"""

import sys


def s_or_u(reactor: list[int]) -> bool:
    """Return whether a reactor report is *safe*.

    A report is safe when every pair of adjacent levels differs by
    1, 2, or 3 in the **same** direction — i.e. the sequence is
    strictly monotonic with a step size in ``[1, 3]``.

    :param reactor: Sequence of integer levels read from one report line.
    :type reactor: list[int]
    :returns: ``True`` if the report is safe, ``False`` otherwise.
    :rtype: bool

    :Example:

    >>> s_or_u([1, 3, 6, 7, 9])
    True
    >>> s_or_u([1, 2, 7, 8, 9])
    False
    """
    # Pairwise differences between consecutive levels.
    diff = [reactor[i+1] - reactor[i] for i in range(len(reactor) - 1)]
    # Strictly increasing by 1..3.
    if all(1 <= d <= 3 for d in diff):
        return True
    # Strictly decreasing by 1..3.
    elif all(-3 <= d <= -1 for d in diff):
        return True
    else:
        return False

safe = 0
with open("input.txt") as f:
    for line in f:
        # Skip blank trailing lines, if any.
        if not line:
             continue
#        print(f"Checking {line.strip()}")
        levels = list(map(int, line.split()))
        if s_or_u(levels):
             safe += 1

print(f"Safe: {safe}")
