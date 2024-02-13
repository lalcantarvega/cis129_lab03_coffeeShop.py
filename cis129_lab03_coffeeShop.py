# Define prices
MENU = {
    "Coffee": 5,
    "Muffin": 4,
    "Croissant": 3,
    "Tea": 3
}
TAX_RATE = 0.06

# Get user input
print("***************************************")
print("Welcome to Our Coffee and Bakery Shop")
print("***************************************")
num_items = {}
for item in MENU:
    num_items[item] = int(input(f"Number of {item}s bought?\n"))

# Calculate subtotal
subtotal = sum(num_items[item] * MENU[item] for item in num_items)

# Calculate tax
tax = subtotal * TAX_RATE

# Calculate total
total = subtotal + tax

# Display receipt
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
for item in num_items:
    print(f"{num_items[item]} {item}s at ${MENU[item]} each: ${num_items[item] * MENU[item]:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
print("Thank you for visiting! We hope to see you again soon.")
