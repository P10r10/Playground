from pathlib import Path
import json


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        print(f"Welcome back, {user['username']}!")
        print(f"I know that you're {user['age']} years old"
              f" and you like {user['hobby']}.")
    else:
        user = {}
        user["username"] = input("What is your name? ")
        user["age"] = int(input("What is your age? "))
        user["hobby"] = input("What is your hobby? ")

        contents = json.dumps(user)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {user['username']}!")


greet_user()
