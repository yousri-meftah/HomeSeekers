class ContractNotFoundException(Exception):
    def __init__(self):
        self.message = "Contract not found"
        super().__init__(self.message)


class ContractOwnershipException(Exception):
    def __init__(self):
        self.message = "You are not the owner of this contract"
        super().__init__(self.message)


class ContractAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "A contract for this home already exists"
        super().__init__(self.message)
