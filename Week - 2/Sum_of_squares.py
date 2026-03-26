data = list(map(int, input("Enter numbers: ").split()))
squares = [x**2 for x in data]
print("Squares:", squares)