data = list(map(int, input("Enter numbers: ").split()))
threshold = int(input("Enter filter value: "))

filtered = [x for x in data if x > threshold]
print("Filtered Data:", filtered)