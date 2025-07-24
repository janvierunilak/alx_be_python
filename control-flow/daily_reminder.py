print("Hello reminder ")

task=input("Enter your task : ")
priority=input("Priority (high/Medium/ low):").strip().lower()
time_bound=input("Is it time bound (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound=="yes":
            print(f" Reminder : '{task}'is a high priority task that requires immediate attention today! ")
        elif time_bound=="no":
            print(f" Reminder: '{task} ' is not a timebound priority, you can do it when you get a break time.")    

    case "medium":
        if time_bound=="yes":
            print(f" Reminder :'{task}'is a high priority task that requires immediate attention today! ")
        elif time_bound=="no":
            print(f" Reminder : '{task} ' is not a timebound priority, you can do it when you get a break time.")    
    case "low" :
        if time_bound=="yes":
            print(f" Reminder :'{task}'is a high priority task that requires immediate attention today! ")
        elif time_bound=="no":
            print(f" Reminder :'{task} ' is not a timebound priority, you can do it when you get a break time.")    
