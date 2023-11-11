from asyncio import run

from market_analysis.lib.io import parse_args, process_line
from market_analysis.lib.platforms import PlatformStrategies

async def main() -> None:
    args = parse_args()
    line = process_line(args.line)

    await PlatformStrategies[line["platform"]].run(line)

if __name__ == "__main__":
    run(main())