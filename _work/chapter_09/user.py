class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.login_name = ""
        self.roles = []
        self.login_attempts = 0

    def describe_user(self):
        return vars(self)

    def greet_user(self):
        print("Hello,", self.first_name, self.last_name + "!")

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges: str = []

    def set_privileges(self, *privileges):
        self.privileges.extend(privileges)

    def show_privileges(self):
        return self.privileges
