temps = list(map(float, input("Enter temperatures: ").split()))
avg = sum(temps) / len(temps)
print("Average Temperature:", avg)