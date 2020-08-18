"""LCS API CLI."""
import argparse
import json
import logging
import sys

import requests
from requests.exceptions import RequestException

from lcs import __version__


_LOGGER = logging.getLogger(__name__)

URL = "http://localhost:8000"


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="LCS CLI Help", allow_abbrev=False)

    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}",
    )

    parser.add_argument(
        "--url", type=str, default=URL, help=f"Url for the LCS web app (default: {URL}).",
    )

    parser.add_argument("file", metavar="FILE", type=argparse.FileType(), help="JSON data.")

    return parser


def main():
    """Entrypoint for API."""
    parser = _create_parser()

    if len(sys.argv) == 1:
        sys.exit(parser.print_help())

    args = parser.parse_args()
    request_params = {
        "headers": {"Accept": "application/json", "Content-Type": "application/json"},
        "url": "/".join([args.url, "lcs"]),
    }

    with args.file as fd:
        response = requests.post(data=fd, **request_params)

    try:
        print(json.dumps(response.json(), indent=2, sort_keys=True))
    except json.decoder.JSONDecodeError:
        pass
    try:
        response.raise_for_status()
    except RequestException as err:
        sys.exit(err)


if __name__ == "__main__":
    main()
