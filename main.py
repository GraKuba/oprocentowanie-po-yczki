initial_loan = 12000
fixed_instalment = 200
interest_rate = 3
month_number = 1

tpl_message ="Twoja pozostala kwota kredytu to {}. To o {} mniej niz w zeszlym miesiacu."

inflation = float(input())
debt = (1 + (inflation + interest_rate) / 1200) * initial_loan - fixed_instalment
message = tpl_message.format(round(debt, 2), round(initial_loan - debt, 2))
print("Month", month_number, message)
month_number += 1

while month_number <= 24:
    initial_debt = debt
    inflation = float(input())
    debt = (1 + (inflation + interest_rate) / 1200) * debt - fixed_instalment
    debt_change = initial_debt - debt
    message = tpl_message.format(round(debt, 2), round(debt_change, 2))
    print("Month", month_number, message)
    month_number += 1
