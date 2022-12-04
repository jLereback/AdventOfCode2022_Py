import argparse

from datetime import datetime, timedelta, timezone
from importlib import import_module


def run(func, filename="filename"):
    try:
        with open(filename) as f:
            print(func(f))
    except FileNotFoundError:
        print()


if __name__ == "__main__":
    now = datetime.now(timezone(timedelta(hours=+1)))
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", "-d", default=now.day)
    args = parser.parse_args()

    module_name = f"src.py.day{args.day:02}"

    module = import_module(module_name)

    for i in ("part1", "part2"):
        if not hasattr(module, i):
            continue
        print(f"--- {i} ---")
        print("answer:", end="\t")
        run(getattr(module, i), f"data/day{args.day:02}.txt")
