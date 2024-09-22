import math
#place all the values for user input as a float to include decimal places
investment_amount = float(input("Enter your investment amount here: "))
annual_interest_rate = float(input("Enter your annual interest rate here: "))
number_of_years = float(input("Enter number of years here: "))

# Convert annual interest rate to monthly interest rate by first dividing it by 100 as it is a percantage and then by 12
monthly_interest_rate = (annual_interest_rate/100) / 12

# Calculate future investment value using the given formula
#include math.pow directly into your formula as in math.pow(a,b) a=base,b=power
future_investment_value = investment_amount * math.pow((1 + monthly_interest_rate), number_of_years * 12)
#Had issues printing as it is so i specified  the future investment value to be printed as a string
print("Your future investment value is: "+str(future_investment_value))