repeat = "y"
while repeat == "y":
	print("select an operation")
	print("1.+")
	print("2.-")
	print("3.*")
	print("4./")

	oper = input()
	num1 = float(input("enter first number"))
	num2 = float(input("enter second number"))

	if oper == "1":
		print(+ num1 + num2)
	if oper == "2":
		print(+ num1 - num2)
	if oper == "3":
		print(+ num1 * num2)
	if oper == "4":
		while num2 == "0":
			num2 = float(input("enter second number again"))
			if num2 := "0":
				continue
			if num2 != "0":
				print(+ num1 / num2)
	repeat = input("perform another operation?y/n")
	if repeat == "y":
		continue
	if repeat == "n":	
		break
input()