"""
CodingQuest Problem 28: Purchase tickets

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Write your solution below the comment line.
"""

# --- Load the data (don't change this) ---
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Take a look at the first few lines
print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

# --- Your code here ---
print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

# --- Your code here ---
costs = {}

for line in data:
    company, rest = line.split(": ")
    category, amount = rest.split()
    amount = int(amount)

    if company not in costs:
        costs[company] = 0

    if category in ["Seat", "Meals", "Luggage", "Fee", "Tax"]:
        costs[company] += amount
    else:  # Discount or Rebate
        costs[company] -= amount

answer = min(costs.values())

print(answer)
