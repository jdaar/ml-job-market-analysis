import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Job data scraper.')
    parser.add_argument('--line', type=str, required=True, help='Line of data to be processed.')
    return parser.parse_args()