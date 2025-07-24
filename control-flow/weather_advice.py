weather=input("what's the weather like today? (sunny /rainy /cold ): ")

response=weather.strip().lower()
if weather=="sunny":
    print("Wear a t-shirt and sunglass.")
elif weather=="rainy":
    print("Don't forget your umbrella and the rain-coat")
elif weather=="cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry , I don't have recommendations for this weather!")
