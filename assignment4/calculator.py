class myCalculator():
  x = 0
  y = 0
  def __init__(self, in_x, in_y):
    self.x = in_x
    self.y = in_y

  def plus(self):
    result = self.x + self.y
    print('Plus : ', self.x, ' + ', self.y, " = ", result)
  
  def subtraction(self):
    result = self.x - self.y
    print('Subtraction : ', self.x, ' - ', self.y, " = ", result)

  def multiply(self):
    result = self.x * self.y
    print('Multiply : ', self.x, ' x ', self.y, " = ", result)

  def divide(self):
    result = self.x / self.y
    print('divide : ', self.x, ' / ', self.y, " = ", result)

print("=======  Calculator =========")
score = int(input('Please input x : '))
score2 = int(input('Please input y : '))
cal = myCalculator(score,score2)
print("======= Menu =========")
print("Press 1 : Plus")
print("Press 2 : Subtraction")
print("Press 3 : Multiply")
print("Press 4 : divide")

my_operator = int(input('Please input [1-4] for result: '))
if my_operator == 1:
  cal.plus()
elif my_operator == 2:
  cal.subtraction()
elif my_operator == 3:
  cal.multiply()
elif my_operator == 4:
  cal.divide()
else:
  print("Please input [1-4] !!!")
