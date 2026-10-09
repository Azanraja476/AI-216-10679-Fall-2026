food = 450
transport = 200
other = 150
budget = 1000

total = food + transport + other
remaining = budget - total

print("Total expense:", total)
print("Remaining budget:", remaining)

if total < budget:
    print("Status: Within budget")
elif total == budget:
    print("Status: Exactly at budget")
else:
    print("Status: Over budget")