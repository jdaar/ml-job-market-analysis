from market_analysis.lib.platforms import Platforms

def process_line(line: str) -> dict:
    return {
        "url": (splitted_line := line.split(','))[0],
        "platform": Platforms(splitted_line[2]),
        "uuid": splitted_line[3],
    }