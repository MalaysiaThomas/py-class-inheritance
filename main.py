class User:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Welcome - {self.name}")

class FrenchUser(User):
    def greet(self):
        print(f"Bonjour - {self.name}")

class SpanishUser(User):
    def greet(self):
        print(f"Hola - {self.name}")

malaysia = User("Malaysia")
matt = FrenchUser("Matthieu")
marcia = SpanishUser("Marcia")

print(malaysia.greet())
print(matt.greet())
print(marcia.greet())