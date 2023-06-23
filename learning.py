from pathlib import Path


path = Path("learning_python.txt")
contents = path.read_text()
print(contents)
for line in contents.splitlines():
    print(line)
print()
contents = contents.replace("Python", "Java")
print(contents)

names = []
while True:
    name = input("What is your name? (q to exit): ")
    if name == "q":
        break
    names.append(name)
path = Path("guest.txt")
path.write_text("\n".join(names))
