daily_usage_kwh = [3.2, 5.0, 7.5, 10.0, 12.4, 4.9, 10.1]

low = 0
normal = 0
high = 0
total = len(daily_usage_kwh)

for val in daily_usage_kwh:
    if val < 5:
        low += 1
    elif val <= 10:
        normal += 1
    else:
        high += 1

print(f"Low: {low} ({(low/total)*100:.2f}%)")
print(f"Normal: {normal} ({(normal/total)*100:.2f}%)")
print(f"High: {high} ({(high/total)*100:.2f}%)")