from user import User, Admin, Privileges

####################################################################################
###     User section
####################################################################################
# users = []
# for i in range(1,4):
#     print()
#     user = User(f"user{i}'s first name", f"user{i}'s last name")
#     user.greet_user()
#     print(user.describe_user())
#     users.append(user)
#     print()

# andrew = User("andrew", "kov")
# print(andrew.describe_user())

# print(f"Login attempts before: {andrew.login_attempts}")
# [andrew.increment_login_attempt() for _ in range(3)]
# print(f"Login attempts after: {andrew.login_attempts}")

# print("Resetting loging attempts...")
# andrew.reset_login_attempts()
# print(f"Login attemts after reset: {andrew.login_attempts}")

####################################################################################
###     Admin section
####################################################################################
dima = Admin("dima", "korobov")
dima.privileges.set_privileges("add post", "delete post", "ban user")
print(dima.describe_user())
print(f"Priveleges: {dima.privileges.show_privileges()}")

anton = Admin("anton", "kovrigin")
anton.privileges.set_privileges("create user", "delete user", "domain administrator")
print(anton.describe_user())
print(
    f"{anton.first_name} {anton.last_name} priveleges: {anton.privileges.show_privileges()}".title()
)
