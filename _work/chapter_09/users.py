import random

class User:


    def __init__(self, first_name, last_name, *user_roles) -> None:
        self.first_name = first_name
        self.last_name = last_name
        if not user_roles:
            user_roles = []
        self.user_roles: list = list(user_roles)

        self.login_attempts = 0

    def add_role(self, role):
        # print("type of {list(self.user_roles)} is", type(set(list(self.user_roles))))
        if role not in self.user_roles:
            self.user_roles.append(role)

    def __repr__(self) -> str:
        return f"User: {self.first_name} {self.last_name}, Roles: {', '.join(self.user_roles)}"
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    

    
user1 = User('andy', 'kov', "admin", "data entry")
print()
print(vars(user1))

print(f"\n{user1} login attempts:", user1.login_attempts)

increment = 5
print(f"\nIncrementing login attempts for the {user1.last_name + ", " +user1.first_name} by {increment}")
[user1.increment_login_attempts() for _ in range(increment)]

print(f"\nuser {user1} login attempts after the increment:", user1.login_attempts, )

print(vars(user1))

print("\nsetting login attempts to 0\n")
user1.reset_login_attempts()
print(vars(user1))


# users: list[User] = []

# for i in range(1, 4):
#     user = User(f"u{i}_fname", f"u{i}_lname", "admin")
#     print(repr(user))   
#     users.append(user)

# for user in users:
#     setattr(user, 'age', random.randint(18,67))
#     print(vars(user))

# user10 = User("u10_fname", "u10_lname")
# print(repr(user10))
# user10.add_role("admin")
# setattr(user10, 'title', "CEO")
# print(vars(user10))


# user1 = User("u1_fname", "u1_lname", "admin")
# print(repr(user1))
# user1.add_role("operator")
# print(repr(user1))
# # breakpoint()
# user1.add_role("manager")
# print(repr(user1))
