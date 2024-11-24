"""
# This program asks the user to input a fraction (X/Y) to represent the fuel level.
# It then calculates the percentage of fuel, shows a message if it's nearly empty (E) or full (F),
# and handles errors like invalid input or division by zero.
"""

def fuel():
    # Keep asking until a valid fraction is entered
    while True:
        try:
            # Ask user to input a fraction
            fraction = input("Enter the fuel amount as a fraction (X/Y): ")
            
            # Split the fraction into two parts
            x, y = fraction.split('/')
            
            # Convert to integers and check validity
            x = int(x)  # Convert numerator to integer
            y = int(y)  # Convert denominator to integer
            
            # Check for invalid inputs
            if y == 0:
                print("Oops! The denominator cannot be zero. Try again.")
                continue
            
            if x > y:
                print("Oops! The numerator cannot be larger than the denominator. Try again.")
                continue
            
            # Calculate percentage and round to nearest integer
            percentage = round((x / y) * 100)
            
            # Determine output based on percentage: 'E' means Empty whereas 'F' means Full
            if percentage <= 1:
                print("E")  
            elif percentage >= 99:
                print("F")  
            else:
                print(f"{percentage}% full")  # Print percentage
            
            # Exit the loop if successful
            break
        
        except ValueError:
            # Handle any errors in conversion like non-integer input
            print("Invalid input. Please enter the fraction as two integers separated by a '/'.")
        except ZeroDivisionError:
            # Handle division by zero (though this is already caught earlier)
            print("Error: Cannot divide by zero.")

# Run the function to get results
fuel()