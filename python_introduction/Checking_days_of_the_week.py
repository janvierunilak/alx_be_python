day=input("Enter a day of the week(Monday-Sunday):").lower()

match day:
    case "monday":
        print("Ughs!,Mondays...")
    case "tuesday":
        print("Just Onother workday!")
    case "wednesday":
        print("Hump day. >>")
    case "thursday":
        print("One more day to go for work") 
    case "friday":
        print("Almost there in the weekend...TGIF!!")
    case "saturday" |"Sunday":
        print("Weekend vibes!!!")
    case _:
        print("Invalid day input")               