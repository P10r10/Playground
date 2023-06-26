from pathlib import Path


contents = Path("karamazov.txt").read_text(encoding="utf-8")
print(contents.lower().count("the "))
