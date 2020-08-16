"""Exceptions module."""


class LcsApiError(Exception):
    """Base Exception for LCS API."""

    fmt = "{}"

    def __init__(self, *args, **kwargs):
        msg = self.fmt.format(*args, **kwargs)
        super().__init__(self, msg)
