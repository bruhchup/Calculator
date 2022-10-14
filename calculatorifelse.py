import faulthandler


repeat = "y"
while repeat == "y":

	print("select an operation")
	print("1.+")
	print("2.-")
	print("3.*")
	print("4./")
	print("5.x**y")
	print("6.√x")
	print("7.y√x")

	while True:
		try:
			oper = int(input())
			break
		except ValueError:
			print("invalid operation")
			print("select an operation")
		continue
	
	if oper < 1 or oper > 7 or oper == "":
		print("invalid operation")
		continue	

	while True:
		try:
			num1 = float(input("enter first number"))
			print(num1)
			break
		except ValueError:
			print("invalid input")	
		
	while oper != 6:
		try:
			num2 = float(input("enter second number"))
			print(num2)
			break
		except ValueError:
			print("invalid input")
	
	if oper == 1:
			print(+ num1 + num2)
	elif oper == 2:
			print(+ num1 - num2)
	elif oper == 3:
			print(+ num1 * num2)
	elif oper == 4:
			if num2 != 0:
				print(num1 / num2)
			if num2 == 0:
				print("Undefined")
	elif oper == 5:
		try:	
			print(num1 ** num2)	
		except OverflowError:
			print("OverFlowError: result too large")
	elif oper == 6:
			comp = (num1 ** (1/2))	
			print ((comp.imag),"j")
	elif oper == 7:
			print (num1 ** (1/num2))

	while repeat := input("perform another operation? y/n"):
		if repeat == "n":
			input("enter any key to terminate program")
			exit()
		if repeat == "y":
			break
		else:
			print(repeat,"is an invalid input")
			continue
	continue
