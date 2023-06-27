import json
from pathlib import Path

if Path("favorite_number.json").exists():
    nb = json.loads(Path("favorite_number.json").read_text())
    print("Your favorite number is", nb)
else:
    number = int(input("What's your favorite number? "))
    Path("favorite_number.json").write_text(json.dumps(number))
