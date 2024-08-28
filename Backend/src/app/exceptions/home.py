class HomeNotFoundException(Exception):
    def __init__(self):
        self.message = "Home not found"
        super().__init__(self.message)


class HomeOwnershipException(Exception):
    def __init__(self):
        self.message = "You are not the owner of this home"
        super().__init__(self.message)


class HomeAddressAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "A home with this address already exists"
        super().__init__(self.message)