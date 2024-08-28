class UserNotFoundException(Exception):
    def __init__(self):
        self.message = "User not found"
        super().__init__(self.message)


class UserEmailAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "Email already exists"
        super().__init__(self.message)


class UserPhoneAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "Phone number already exists"
        super().__init__(self.message)


class InvalidUserPasswordException(Exception):
    def __init__(self):
        self.message = "Invalid password"
        super().__init__(self.message)