
from datetime import datetime, timedelta


def display_Current_date_time():
    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(" Current Date and Time is : ", formatted_date)


def calculate_future_date():

    try:

        num_days = int(input("Enter the number of future days :"))
        current_date = datetime.now().date()

        future_date = current_date + timedelta(days=num_days)

        formated_future_date = future_date.strftime("%Y-%m-%d")
        print(f"The future date will be : {formated_future_date}")

    except ValueError:
        print("Invalid input ! Enter an integer number !")


if __name__ == "__main__":
    display_Current_date_time()
    calculate_future_date()
