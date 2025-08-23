day = "Saturdae"

match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case "Monday":
        print("Start of the week")
    case _:
      print("Weekday")
