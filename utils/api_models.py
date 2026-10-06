class UserResponse:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.username = data["username"]
        self.email = data["email"]