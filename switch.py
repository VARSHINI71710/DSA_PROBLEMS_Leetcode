color = input("Enter a colour from three colours (red/yellow/green): ").lower()

match color:
    case"red":
        print("Stop")
    case"yellow":
        print("Ready")
    case"green":
        print("Go")
    case _:
        print("Invalid color! Please enter red, yellow, or green.")
