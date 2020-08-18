"""Configuration for tests."""
import lcs


def pytest_report_header():
    """Additional report header."""
    return f"version: {lcs.__version__}"
