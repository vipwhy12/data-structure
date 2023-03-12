

class Person :
  def __init__(self, prameter_name):
    self.name = prameter_name
    
  def my_name_is(self):
    print("Hello my name is " + self.name )
    
    
person_1 = Person("노하나")
print(person_1.name)

person_1.my_name_is()

person_2 = Person("노유나")
print(person_2.name)

person_2.my_name_is()