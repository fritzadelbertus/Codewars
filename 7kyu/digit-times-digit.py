# Codewars: Digit*Digit
# Source: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

square_digits = lambda x: int(''.join([str(int(i)**2) for i in str(x)]))

print(square_digits(765))
