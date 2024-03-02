num1 = float(input("Enter the first number: "))
operator = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == "+":
  result = num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == "/":
 
  if num2 == 0:
    print("Error: Cannot divide by zero.")
  else:
    result = num1 / num2
else:
  print("Invalid operation. Please choose +, -, *, or /.")
 
  exit()
if operator != "/":  
  print(f"{num1} {operator} {num2} = {result}")
