"""Pytest plugin for grading.

Supports the `points` marker to assign point values to tests, and
generates a summary of points earned at the end of the test run."""

import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "points(value): assign point value to a test for grading"
    )


def pytest_collection_modifyitems(config, items):
    points = {}
    for item in items:
        m = item.get_closest_marker('points')
        if m:
            points[item.nodeid] = m.args[0]
        else:
            points[item.nodeid] = 0
    config.points = points


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    passed_reports = [
            report for report in terminalreporter.stats.get("passed", [])
            if report.when == 'call' and report.passed
        ]
    total_points = sum(config.points[report.nodeid]
                       for report in passed_reports)
    terminalreporter.write_sep("=", "Grading Summary")
    terminalreporter.write_line(f"Total Points: {total_points}")
