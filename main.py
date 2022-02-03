initial_loan = 12000
fixed_instalment = 200

inflation = float(input())
debt = (1 + (inflation + 3) / 1200) * initial_loan - fixed_instalment
print(debt)





