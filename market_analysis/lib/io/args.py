import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Job data scraper.")
    parser.add_argument(
        "lines",
        metavar="LINES",
        type=str,
        nargs="+",
        help="Lines of data to be processed.",
    )
    return parser.parse_args()
