# pylint: disable=no-self-use, too-few-public-methods
"""Tests for `lcs` package."""
# TODO: Make proper tests, i.e. fixtures
import logging

from lcs.main import _pmatches, matches


class TestLcs:
    """Tests for `lcs.main` module."""

    def test_pmatch_000(self):
        """First Test run."""
        string1 = "aaaapies- -applxe pies available"
        string2 = "aaaacome have some apple .pies"
        results = _pmatches(string1, string2)
        logging.info(_pmatches.cache_info())
        assert results == {"aaaa", "pies", "appl"}

    def test_matches_duplicate_str(self):
        string1 = "aaaapies- -applxe pies available"
        string2 = "aaaacome have some apple .pies"
        strings = [
            string1,
            string2,
            string1,
            string2,
            string1,
        ]
        results = matches(strings)
        logging.info(_pmatches.cache_info())
        assert list(results) == ["aaaa", "appl", "pies"]

    def test_matches_none(self):
        strings = [
            "aa",
            "ba",
            "bc",
            "dd",
            "ae",
        ]
        results = matches(strings)
        logging.info(_pmatches.cache_info())
        assert not any(results)

    def test_matches_single_letter(self):
        strings = [
            "ab",
            "b",
            "bbc",
            "bc",
            "dbd",
            "bbae",
        ]
        results = matches(strings)
        logging.info(_pmatches.cache_info())
        assert list(results) == [
            "b",
        ]

    def test_matches_single_match(self):
        strings = [
            "aac",
            "aac",
            "aac",
            "aad",
            "ealaad",
        ]
        results = matches(strings)
        logging.info(_pmatches.cache_info())
        assert list(results) == [
            "aa",
        ]
