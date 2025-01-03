# Valid Denominations in a list
valid_denom = [25, 10, 5]
coke_cost = 50
amount_paid = 0

# Loop until coin entered exceeds coke cost
while amount_paid < coke_cost:
    while True:
        print(f"Amount Due: {coke_cost - amount_paid}")
        coin = int(input("Insert Coin: "))
        if coin in valid_denom:
            amount_paid += coin
            break

# Print the change owed by the machine to the user
print(f"Change Owed: {amount_paid - coke_cost}")
