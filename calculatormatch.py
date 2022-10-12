print("Addition and Subtr Calculator")
retry = "y"
while retry == "y":
	select = input('')
	num1 = float(input("enter first number"))
	num2 = float(input("enter second number"))
	match select:
		case '+':
			print(add(num1, num2))
			input() 
		case '-':
			
		case other:
			print ('No')
	retry = input("Perform another operation? y/n")
	if retry == "y":
		continue
	if retry == "n":
		break