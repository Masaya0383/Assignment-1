# Masaya Sugimoto Assignment 1B

Balance = float(input('Please enter the starting balance ($): '))

Years = int(input('Enter the term (years):'))

int_rate = float(input('Enter the interest rate (%):'))

comp_freq = int(input('Enter the compounding frequency (times/year): '))

future_value = Balance * (1 + ((int_rate/100) / comp_freq)) ** ( comp_freq * Years)

print(f'An initial investment of {Balance}, in {Years} years, at an interest rate of {int_rate}% , compounded at {comp_freq} times per year, will be worth {future_value}')
