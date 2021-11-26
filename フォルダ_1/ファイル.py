class anal_分析する():
	 def __init__(self, name, age):
		 self.name = name
		 self.age = age
		 
	 def 印刷(self):
		 print('Hey! ' +self.name +', '+self.age)

class 継承(anal_分析する):
	def __init__(self, name, age):
		super().__init__(name, age)


x = 継承("Dan", "14")