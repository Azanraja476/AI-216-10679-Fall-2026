usage = float(input("Enter data usage in GB: "))

if usage < 0:
    print("Invalid — usage cannot be negative")
elif usage <= 5:
    print("Basic")
elif usage <= 15:
    print("Standard")
else:
    print("Premium")