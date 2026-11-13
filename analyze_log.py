from collections import Counter
from pathlib import Path

log_file = Path(__file__).parent / "ingest.log"
levels = Counter()

with open(log_file, encoding="utf-8") as f:
    for line in f:
        parts = line.split("|")
        if len(parts) >= 2:
            levels[parts[1].strip()] += 1

print(levels)
print(f"total lines: {sum(levels.values())}")
