class PostNotFoundException(Exception):
    def __init__(self):
        self.message = "Post not found"
        super().__init__(self.message)


class PostOwnershipException(Exception):
    def __init__(self):
        self.message = "You are not the owner of this post"
        super().__init__(self.message)


class PostInactiveException(Exception):
    def __init__(self):
        self.message = "This post is inactive"
        super().__init__(self.message)