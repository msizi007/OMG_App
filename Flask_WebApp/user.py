
class User:
    def __init__(self, username: str, password: str, id: int=0):
        self.id = id
        self.username = username
        self.password = password
