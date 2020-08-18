# pylint: disable=no-self-use, too-few-public-methods
"""Tests for `lcs` package."""
# TODO: Make proper tests, i.e. fixtures
# TODO: Test bad data
import logging

from starlette.testclient import TestClient

from lcs.web import app


CLIENT = TestClient(app)


class TestApi:
    """Tests for `lcs.api` module."""

    def test_home(self):
        """Are we alive?"""
        response = CLIENT.get("/")
        logging.debug(response.reason)
        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"

    def test_post_good(self):
        """Integration test."""
        data = {
            "setOfStrings": [
                {"value": "comcast"},
                {"value": "comcastic"},
                {"value": "broadcaster"},
            ]
        }
        response = CLIENT.post("/lcs/", json=data)
        logging.debug(response.reason)
        assert response.status_code == 200
        assert response.json() == {"lcs": [{"value": "cast"}]}
