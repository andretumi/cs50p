coke_price = 50
amount_due = coke_price
owed_to_customer = 0
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    inserted_coin = int(input("Insert Coin: "))
    match inserted_coin:
        case 25:
            amount_due -= 25
        case 10:
            amount_due -= 10
        case 5:
            amount_due -= 5
    if amount_due < 0:
        owed_to_customer = abs(amount_due)
print(f"Change Owed: {owed_to_customer}")
