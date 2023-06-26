from pathlib import Path

path1 = Path("cats.txt")
path2 = Path("dogs1.txt")

try:
    content1 = path1.read_text()
except FileNotFoundError:
    print(f"The file {path1} is missing.")
else:
    print(content1)
try:
    content2 = path2.read_text()
except FileNotFoundError:
    print(f"The file {path2} is missing.")
else:
    print(content2)
