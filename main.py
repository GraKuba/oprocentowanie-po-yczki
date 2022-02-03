initial_loan = 12000
fixed_instalment = 200

inflation = float(input())

debt = (1 + (inflation + 3) / 1200) * 12000 - 200

print(debt)




