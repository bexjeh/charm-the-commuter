"""Charm the Commuter: Forecast a City That Isn't.

Writes exactly one line of weather forecast for the invented city of
Slantwell to MAKEFUN_OUTPUT_DIR/entry.txt (fallback ".").
Deterministic, self-contained, no network, no clock, no env, no model calls.
"""

import os

FORECAST = (
    "In Slantwell, rain falls sideways all morning, so the 8:15 bus "
    "arrives bone-dry while everyone waiting for it is soaked to the skin."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
