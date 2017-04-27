# Factorial

def factorial(number):
	"""Given a number, returns its factorial"""
	if number==0 or number==1:
		return 1
	answer = number*factorial(number-1)
	return answer
	
thing = int(input("Give me an integer to find the factorial. "))
print("The factorial of {} is {}.".format(thing,factorial(thing)))


# Multiply

def multiply(number,other):
	if other == 0:
		return 0
	sum = number + multiply(number,other-1)
	return sum
	
one = int(input("Give me a number to multiply. "))
two = int(input("Give me another number to multiply with the first. "))

print("{} times {} equals {}.".format(one,two,multiply(one,two)))