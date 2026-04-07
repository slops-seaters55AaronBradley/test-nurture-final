"""Main module - updated."""

import sys

def hello(name="world"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    hello(sys.argv[1] if len(sys.argv) > 1 else "world")
