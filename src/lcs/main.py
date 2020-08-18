"""Main functions for LCS logic."""
import logging
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from difflib import SequenceMatcher
from functools import lru_cache
from itertools import chain
from typing import Sequence


@lru_cache()
def _pmatches(str1: str, str2: str, size: str = -1) -> Sequence[str]:
    logging.debug("str1=%s, str2=%s, size=%s", str1, str2, size)
    if str1 == str2:
        return {
            str1,
        }

    match = SequenceMatcher(a=str1, b=str2).find_longest_match(0, len(str1), 0, len(str2))

    if not match.size or match.size < size:
        return set()

    results = deque([str1[match.a : match.a + match.size]])
    if match.a <= match.b:
        str_a, str_b = str1[match.a + match.size :], str2
    else:
        str_a, str_b = str1, str2[match.b + match.size :]
    results.extend(_pmatches(str_a, str_b, match.size))

    return set(results)


def _matches(strings: Sequence[str]) -> Sequence[str]:
    """Return set of longest common strings."""
    total_str = len(strings)

    if total_str <= 1:
        return set(*strings)

    unchecked_str = strings[-1] if total_str % 2 else None
    str_pairs = zip(*[iter(strings)] * 2)

    # Note: The over head of threads pools may be slower than comprehension for smaller sequences.
    # results = deque(starmap(_matches_from_pair, pairs))
    with ThreadPoolExecutor() as executor:
        results = deque(executor.map(lambda i_: _pmatches(*i_), str_pairs))

    # Add set of matches from the unchecked string.
    if unchecked_str and results:
        unchecked_matches = set(
            chain.from_iterable(_pmatches(i_, unchecked_str) for i_ in results[0])
        )
        results.append(unchecked_matches)

    logging.debug("results=%s", results)
    # We know there are no matches as soon as we see the first empty set.
    if not all(results):
        return set()

    common_matches = set(results[0])
    for i_ in results:
        common_matches.intersection_update(i_)

    # If there is a common match, that will be the longest substring
    return (
        common_matches if common_matches else set(_matches(deque(chain.from_iterable(results))))
    )


def matches(strings: Sequence[str]) -> Sequence[str]:
    """Return set of longest common strings."""
    return deque(sorted(_matches(strings)))


if __name__ == "__main__":
    raise RuntimeError()
