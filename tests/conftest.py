"""Configuration for tests."""
import lcs_api


def pytest_report_header():
    """Additional report header."""
    return f"version: {lcs_api.__version__}"
