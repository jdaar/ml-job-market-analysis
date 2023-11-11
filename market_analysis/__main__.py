from asyncio import run
from itertools import groupby

from market_analysis.lib.io import parse_args, process_line
from market_analysis.lib.platforms import PlatformStrategies


async def main() -> None:
    args = parse_args()
    lines = [process_line(line) for line in args.lines]

    grouped_lines = groupby(lines, lambda line: line["platform"])
    for platform, group in grouped_lines:
        await PlatformStrategies[platform].run(list(group))


if __name__ == "__main__":
    run(main())
