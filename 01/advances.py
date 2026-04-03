# Create a list
fruits = ["apple", "banana", "orange"]

# Add an item
fruits.append("grape")

# Remove an item
fruits.remove("banana")

# Access items by index
print(fruits[0])  # Output: apple

# Loop through the list
for fruit in fruits:
    print(fruit)

# List length
print(len(fruits))  # Output: 3

# Set example
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.discard("green")
print("red" in colors)  # True
for color in colors:
    print(color)
print(len(colors))  # Output: 3
# Dictionary example
person = {"name": "Alice", "age": 30, "city": "Seattle"}
person["email"] = "alice@example.com"
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 30
for key, value in person.items():
    print(key, value)
print(len(person))  # Output: 4