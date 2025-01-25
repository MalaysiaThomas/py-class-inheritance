from user import User

class FrenchUser(User):
    def greet(self):
        return(f"Bonjour - {self.name}")