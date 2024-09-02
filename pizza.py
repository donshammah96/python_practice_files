def order_pizza(size, *toppings, **details):
    print(f"Ordering a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

    print("\nDetails of the order are: ")
    for key, value in details.items():
        print(f"{key}: {value}")

order_pizza(12, "pepperoni", "mushrooms", "green peppers", "extra cheese", Name="Don", Address="12421 Yellow Wood Drive", Phone="555-1234")