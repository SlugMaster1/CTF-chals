#!/usr/bin/python2
from math import exp
from scipy.integrate import quad

def factorial(n):
  f = 1
  if n < 0:
    n += 1
    while n < 1:
      f /= n
      n += 1
  else:
    while n > 1:
      f *= n
      n -= 1
  return f
  
def gamma(n):
  r = lambda z : pow(z,n) * exp(-z)
  return quad(r,0,100,full_output=1)[0]

try:
  print("Welcome to Factorial Calculator!")
  num = input("Please enter a number:\n")
  if(isinstance(num,int) or isinstance(num,long)):
    if(num < 0):
      print(str(num) + "! is undefined")
    elif(num > 100000):
      print("Please enter a smaller number.")
    else:
      print(str(num) + "! = " + str(factorial(num)))
  elif(isinstance(num,float)):
    if(abs(num) > 100000):
      print("Please enter a smaller number.")
    else:
      print(str(num) + "! = " + str(gamma(num%1)*factorial(num)))
  else:
    print("\'" + str(num) + "\' is not a number.")
except:
  print("That is not a number")
