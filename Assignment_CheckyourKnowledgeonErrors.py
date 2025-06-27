# Task 1 - Understanding Python Exceptions


print("Task 1: Division Calculator\n")

while True:
   try:
      
       user_input = input("Enter a number: ")
       
      
       number = float(user_input)
       
       
       result = 100 / number
       
       
       print(f"100 divided by {number} is {result}")
       break  
   except ZeroDivisionError:
       
       print("Oops! You cannot divide by zero.")
       
   except ValueError:
      
       print("Invalid input! Please enter a valid number.")

print("\n" + "-" * 40 + "\n")  

# Task 2 - Types of Exceptions

print("Task 2: Demonstrating Different Exception Types\n")


try:
  
   my_list = [1, 2, 3]
   
   
   print(my_list[3])
   
except IndexError:
 
   print("IndexError occurred! List index out of range.")

# Example 2: KeyError
try:
  
   my_dict = {"name": "Alice", "age": 25}
   
   print(my_dict["address"])
   
except KeyError:
  
   print("KeyError occurred! Key not found in the dictionary.")

# Example 3: TypeError
try:
   
   result = "hello" + 5
   
except TypeError:
  
   print("TypeError occurred! Unsupported operand types.")

print("\n" + "-" * 40 + "\n")  # Separator between tasks

# Task 3 - Using try...except...else...finally

print("Task 3: Division with Complete Exception Handling\n")

try:
   
   num1 = float(input("Enter the first number: "))
   num2 = float(input("Enter the second number: "))
   
  
   result = num1 / num2
   
except ValueError:
   
   print("Error: Please enter valid numbers.")
   
except ZeroDivisionError:
  
   print("Error: Cannot divide by zero.")
   
else:
  
   print(f"The result is {result}.")
   
finally:
  
   print("This block always executes.")