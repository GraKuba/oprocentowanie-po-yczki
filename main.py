initial_loan = 12000
fixed_instalment = 200
intrest_rate = 3

tpl_message = message ="Twoja pozostala kwota kredytu to {}. To o X mniej niz w zeszlym miesiacu."

inflation = float(input())
debt = (1 + (inflation + intrest_rate) / 1200) * initial_loan - fixed_instalment
message = tpl_message.format(debt)
print(message)

inflation = float(input())
debt = (1 + (inflation + intrest_rate) / 1200) * debt - fixed_instalment
message = tpl_message.format(debt)
print(message)




