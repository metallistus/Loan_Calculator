income = int(input())
percent = 0
first_max = 15527
second_max = 42707
third_max = 132406
if income <= first_max:
    percent = 0
elif income <= second_max:
    percent = 15
elif income <= third_max:
    percent = 25
else:
    percent = 28
calculated_tax = round(income / 100 * percent)

print('The tax for {0} is {1}%. That is {2} dollars!'.format(income, percent, calculated_tax))