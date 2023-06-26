while True:
    try:
        n1 = int(input("Number 1? (-1 to quit) "))
        if n1 == -1:
            break
        n2 = int(input("Number 2? (-1 to quit) "))
        if n2 == -1:
            break
    except ValueError:
        print("You didn't insert a valid number.")
    else:
        print(n1 + n2)
