'''5. Check if a given number is an Armstrong number or not.
(Amazon) '''

num = int(input("Enter a number: "))

# Convert the number to string to count digits easily
num_str = str(num)
num_digits = len(num_str)

# Compute the sum of digits raised to the power of num_digits
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")


