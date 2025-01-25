from user import User

class SpanishUser(User):
    def greet(self):
        return(f"Hola - {self.name}")