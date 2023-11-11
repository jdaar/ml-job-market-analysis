import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Job data scraper.')
    parser.add_argument('--line', type=str, required=True, help='Line of data to be processed.')
    return parser.parse_args()

def process_line(line):
    return {
        "url": (splitted_line := line.split(','))[0],
        "platform": splitted_line[2],
        "uuid": splitted_line[3],
    }

def main():
    args = parse_args()
    print(process_line(args.line))

main()