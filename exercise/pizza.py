def make_pizza(size,*toppings):
    print(f"\n make a {size}-inch pizza with ")
    for topping in toppings:
        print(f"-{topping}")