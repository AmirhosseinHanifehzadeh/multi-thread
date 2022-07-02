number = 123
sum_of_digits = 0
for digit in str(number): #turn to string to iterate through.
    sum_of_digits += int(digit)
print(sum_of_digits)