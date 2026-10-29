from functools import reduce

numbers = [40, 60, 80, 120]

# Step 1: Double each number 
doubled = list(map(lambda x: x * 2, numbers))

# Step 2: Keep only numbers greater than 100
filtered = list(filter(lambda x: x > 100, doubled))

# Step 3: Calculate the sum
total = reduce(lambda a,b : a + b, filtered)

print("Doubled numbers:", doubled)
print("Filtered numbers:", filtered)
print("Final sum:", total)