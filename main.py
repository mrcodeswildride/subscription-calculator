print()

monthly_cost = float(input("Enter a monthly cost: $"))
yearly_cost = monthly_cost * 12
print(f"The yearly cost is ${yearly_cost:.2f}.\n")

yearly_cost = float(input("Enter a yearly cost: $"))
monthly_cost = yearly_cost / 12
print(f"The monthly cost is ${monthly_cost:.2f}.")
