temperatures = [21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]

below = 0
normal = 0
high = 0

for temp in temperatures:
    if temp < 15:
        print(temp, "-> Below Normal")
        below += 1
    elif temp <= 30:
        print(temp, "-> Normal")
        normal += 1
    else:
        print(temp, "-> High")
        high += 1

print("\nSummary:")
print("Below Normal:", below)
print("Normal:", normal)
print("High:", high)