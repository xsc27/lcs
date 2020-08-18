"""Module interface for LCS API."""
import logging
import sys

from lcs.cli.cmd import main as cli


def main():
    """Entrypoint to aoad as Python module."""
    module_args = sys.argv[1:]
    logging.debug("Module arguments received: %s", module_args)
    cli()


if __name__ == "__main__":
    main()
