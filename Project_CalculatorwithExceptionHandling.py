import logging

# Configure logging to write to a file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                   format='%(asctime)s - %(levelname)s: %(message)s')

def get_valid_number(prompt):
   """
   Function to get a valid number from the user.
   Continues to prompt until valid input is received.
   """
   while True:
       try:
           # Try to convert the input to a float
           return float(input(prompt))
       except ValueError:
           # Handle invalid input
           print("Invalid input! Please enter a valid number.")
           # Log the error
           logging.error("ValueError occurred: Invalid input for number.")

def add(a, b):
   """Function to add two numbers"""
   return a + b

def subtract(a, b):
   """Function to subtract two numbers"""
   return a - b

def multiply(a, b):
   """Function to multiply two numbers"""
   return a * b

def divide(a, b):
   """Function to divide two numbers with error handling"""
   try:
       return a / b
   except ZeroDivisionError:
       # Handle division by zero
       print("Oops! Division by zero is not allowed.")
       # Log the error
       logging.error("ZeroDivisionError occurred: division by zero.")
       return None

def main():
   """Main function to run the calculator program"""
   print("Welcome to the Error-Free Calculator!")
   
   while True:
       # Display menu
       print("\nChoose an operation:")
       print("1. Addition")
       print("2. Subtraction")
       print("3. Multiplication")
       print("4. Division")
       print("5. Exit")
       
       try:
           # Get user choice
           choice = input("> ")
           
           # Check if the user wants to exit
           if choice == '5':
               print("Goodbye!")
               break
           
           # Validate the choice
           if choice not in ['1', '2', '3', '4']:
               print("Invalid choice! Please enter a number between 1 and 5.")
               continue
           
           # Get the numbers for calculation
           num1 = get_valid_number("Enter the first number: ")
           num2 = get_valid_number("Enter the second number: ")
           
           # Perform the selected operation
           if choice == '1':
               result = add(num1, num2)
               print(f"Result: {num1} + {num2} = {result}")
           elif choice == '2':
               result = subtract(num1, num2)
               print(f"Result: {num1} - {num2} = {result}")
           elif choice == '3':
               result = multiply(num1, num2)
               print(f"Result: {num1} * {num2} = {result}")
           elif choice == '4':
               result = divide(num1, num2)
               if result is not None:
                   print(f"Result: {num1} / {num2} = {result}")
       
       except Exception as e:
           # Catch any unexpected exceptions
           print(f"An unexpected error occurred: {e}")
           logging.error(f"Unexpected error: {type(e).__name__} - {e}")
           
       finally:
           # This will always execute
           print("Thank you for using the calculator!")

# Run the program
if __name__ == "__main__":
   try:
       main()
   except KeyboardInterrupt:
       # Handle if user presses Ctrl+C
       print("\nProgram terminated by user.")
       logging.warning("Program terminated by user (KeyboardInterrupt).")
   except Exception as e:
       # Handle any other unexpected exceptions
       print(f"\nAn unexpected error occurred: {e}")
       logging.critical(f"Critical error: {type(e).__name__} - {e}")
       print("The program will now exit.")