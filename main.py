class Person():
	def __init__(self):
		self.name = "John"
	def display(self):
		print("My name is: ", self.name)

class Child(Person):
	def __init__(self):
		super().__init__()

	def display2(self):
		super().display()
		print("test")

test = Child()
test.display2()
"test"
