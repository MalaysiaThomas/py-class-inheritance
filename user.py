class User:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return(f"Welcome - {self.name}")