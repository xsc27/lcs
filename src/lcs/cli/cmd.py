"""LCS CLI."""
import argparse
import logging
import sys

from lcs import __version__, matches


_LOGGER = logging.getLogger(__name__)


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="LCS CLI Help", allow_abbrev=False)

    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}",
    )

    parser.add_argument("string", metavar="STRING", type=str)
    parser.add_argument(
        "strings",
        metavar="STRING",
        type=str,
        nargs="+",
        help="Strings to be queried (at least 2).",
    )

    return parser


def main():
    """Entrypoint for console."""
    parser = _create_parser()

    if len(sys.argv) == 1:
        sys.exit(parser.print_help())

    args = parser.parse_args()
    strings = args.strings
    strings.append(args.string)
    print(list(matches(strings)))


if __name__ == "__main__":
    main()
