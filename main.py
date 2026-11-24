"""Entry for One Word From Your Ex (make.fun).

Writes one word an ex would use to describe you, to /output/entry.txt.
"""
import os

ENTRY = "unforgettable"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
