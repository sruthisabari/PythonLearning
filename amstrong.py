def is_armstrong_number(number):
    # Step 1: Count the number of digits
    n = len(str(number))
    
    # Step 2: Split the number into its digits
    temp = number
    sum_of_powers = 0
    
    while temp > 0:
        digit = temp % 10  # Extract the last digit
        temp //= 10  # Move to the next digit
        sum_of_powers += digit ** n  # Step 3
    
    # Step 5: Check for equality
    return sum_of_powers == number

# Example usage:
number_to_check = 169
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")
