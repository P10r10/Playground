from restaurants import User


class Admin(User):
    def __init__(self, first_name, last_name, age, privileges: list[str]):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges: list[str]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:\n", ", ".join(self.privileges))


privileges = [
    "can add post",
    "can delete post",
    "can ban user",
]


admin = Admin("Almeida", "Santiago", 49, privileges)
admin.privileges.show_privileges()
