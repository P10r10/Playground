import admin

my_admin = admin.Admin("Almeida", "Santiago", 49, privileges=[
    "can add post",
    "can delete post",
    "can ban user",
])

my_admin.privileges.show_privileges()
