





while True:
    try:
        users_choice = int(input("What times tables do you want? "))
    except ValueError:
        print("Invalid entry, must be a whole number ")
        continue
    else:
        for i in range(1, 13):
            table = i * users_choice
            print(f"{users_choice} times {i} = {table} ")
            
    try_again = input("Do you want another go? (y/n)")

    if try_again.lower() == "n":
        break
    elif try_again != "y":
        print("Please enter either Y/N")
        