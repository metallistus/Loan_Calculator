import argparse
import math


def check_positive(value):
    value = float(value)
    if value <= 0.0:
        print("Incorrect parameters")
    return value


def check_diff_annuity(value):
    list_type = ["diff", "annuity"]
    if value not in list_type:
        print("Incorrect parameters")
    return value


def loan_principal():
    interest = args.interest / 12 / 100
    calc_loan_principal = args.payment / ((interest * (1 + interest) ** args.periods) /
                                          (((1 + interest) ** args.periods) - 1))
    overpayment = args.periods * args.payment - calc_loan_principal
    print('Your loan principal = {}!'.format(math.floor(calc_loan_principal)))
    print('Overpayment = {}'.format(overpayment))


def number_of_month():
    nominal_interest_rate = args.interest / (12 * 100)
    number_of_payments = math.log(
        (args.payment / (args.payment - nominal_interest_rate * args.principal)),
        1 + nominal_interest_rate)
    number_of_payments = int(math.ceil(number_of_payments))
    if number_of_payments <= 12:
        print('It will take {} months to repay this loan!'.format(number_of_payments))
    elif number_of_payments > 12:
        years = math.floor(number_of_payments / 12)
        months = number_of_payments % 12
        print('It will take {} years and {} months to repay this loan!'.format(years, months))
    overpayment = number_of_payments * args.payment - args.principal  # think about formula
    print('Overpayment = {}'.format(overpayment))


def annuity_monthly_payment():
    args.interest = args.interest / 12 / 100
    monthly_payment = args.principal * ((args.interest * (1 + args.interest) ** args.periods) /
                                        (((1 + args.interest) ** args.periods) - 1))
    print('Your monthly payment = {}!'.format(math.ceil(monthly_payment)))


def diff_payment():
    nominal_interest_rate = args.interest / (12 * 100)
    current_month = 1
    list_month_payments = []
    while current_month < args.periods + 1:
        month_diff_payment = (args.principal / args.periods) + (nominal_interest_rate * (args.principal -
                                                                (args.principal * (current_month - 1)) / args.periods))
        list_month_payments.append(math.ceil(month_diff_payment))
        print("Month {}: payment is {}".format(current_month, month_diff_payment))
        current_month = current_month + 1
    print()
    sum_month_payments = sum(list_month_payments)
    overpayment = sum_month_payments - args.principal
    print('Overpayment = {}'.format(overpayment))


# start parser is here
parser = argparse.ArgumentParser()

parser.add_argument("--type", type=check_diff_annuity, required=True)
parser.add_argument("--principal", type=check_positive)
parser.add_argument("--periods", type=check_positive)
parser.add_argument("--interest", type=check_positive)
parser.add_argument("--payment", type=check_positive, default=False)

args = parser.parse_args()

if args.type == "diff" and args.payment == "True":
    print("Incorrect parameters")
if args.interest is None:
    print("Incorrect parameters")
if args.type == "annuity" and args.payment and args.periods and args.interest:
    loan_principal()
if args.type == "annuity" and args.principal and args.payment and args.interest:
    number_of_month()
if args.type == "annuity" and args.principal and args.periods and args.interest:
    annuity_monthly_payment()
if args.type == "diff" and args.principal and args.periods and args.interest:
    diff_payment()
