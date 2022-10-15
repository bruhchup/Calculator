#Attempt at personalizing my project :)
print("HTech©")
#Declares value of repeat to be "y" so while loop can initiate
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
	print("8.exit program")

#Makes variable "oper" only accept integer values. Will loop if ValueError is detected
	while True:
		try:
			oper = int(input())
			break
		except ValueError:
			print("invalid operation")
			print("select an operation")
		continue

#Only allows "oper" to hold an integer value of 1-8 	
	if oper < 1 or oper > 8 or oper == "":
		print("invalid operation")
		continue	

#Allows the 8th operation to bypass num1 input
	while oper != 8:
#Try except prevents ValueError and only allows float input
		try:
			num1 = float(input("enter first number"))
			print(num1)
			break
		except ValueError:
			print("invalid input")	

#Allows operation 6 and 8 to bypass num2 input		
	while oper != 6 and oper != 8:
		try:
#Try except prevents ValueError and only allows float input
			num2 = float(input("enter second number"))
			print(num2)
			break
		except ValueError:
			print("invalid input")
#1.+	
	if oper == 1:
			print(+ num1 + num2)
#2.-
	elif oper == 2:
			print(+ num1 - num2)
#3.*
	elif oper == 3:
			print(+ num1 * num2)
#4./
	elif oper == 4:
#Prevents user input of 0
			if num2 != 0:
				print(num1 / num2)
			if num2 == 0:
				print("Undefined")
#5.x**y
	elif oper == 5:
#solves OverFlowError which causes the program to crash
		try:	
			print(num1 ** num2)	
		except OverflowError:
			print("OverFlowError: result too large")
#6.√x
	elif oper == 6:
			comp = (num1 ** (1/2))	
#Only shows the imaginary number in a complex number
#"j" is used instead of i as Python represents imaginary numbers with a j
			if num1 < 0:
				print((comp.imag),"j")
#If num1 is greater than 0, the solution will not be imaginary, eliminating the need for "j"
			elif num1 > 0:
				print(comp)
#7.y√x
	elif oper == 7:
			print (num1 ** (1/num2))
#8.exit program
	elif oper == 8:
		while True:
			aresure = input("are you sure? y/n")
			if aresure == "y":
				exit()
			if aresure == "n":
				break
			else:
				print (aresure,"is an invalid input")
			continue
		continue
#Displays after operations 1-7
	while True:
		repeat = input("perform another operation? y/n")
		if repeat == "n":
			input("enter any key to terminate program ")
			exit()
		elif repeat == "y":
			break
		else:
			print(repeat,"is an invalid input")
			continue
	continue