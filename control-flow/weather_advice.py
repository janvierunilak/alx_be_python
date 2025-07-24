choose_weather=input("what's the weather like today? (sunny/rainy/cold) : ")

response=choose_weather.strip().lower()
if choose_weather=='sunny':
    print("Wear a t-shirt and sunglass.")
elif choose_weather=='rainy':
    print("Don't forget your umbrella and the rain-coat")
elif choose_weather=='cold':
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry , I don't have recommendations for this weather!")
