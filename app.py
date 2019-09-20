def max_number(numbers):
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

new_max = max_number([17, 13, 25, 0, -2])

#-------------------------------------------

def remove_duplicate(list):
  non_duplicate_list = []
  for item in list:
    if item in non_duplicate_list:
      pass
    else:
      non_duplicate_list.append(item)
  return non_duplicate_list

new_list = remove_duplicate([2, 2, 3, 5, 6, 9, 4, 4, 4])
#print(new_list)

#-------------------------------------------

def greet_user(first_name, last_name):
  print('Hello ' + first_name + ' ' + last_name)

#greet_user(last_name='Mike', first_name='Bickle')

#--------------------------------------------

class Person:
  def __init__(self, name):
    self.name = name
  
  def talk(self):
    print('Hi, I am ' + self.name)

john = Person('John Smith')
bob = Person('Bob Smith')

john.talk()
bob.talk()