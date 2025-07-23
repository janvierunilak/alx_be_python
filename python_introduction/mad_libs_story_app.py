print("Lets play a Mad Lib Story!, PLEASE , answer the following questions:<<::>>:")

name=input("Enter a name:")
noun=input("Enter a noun like (treasure):")
verb=input("Enter a verb : ")
adjective=input("Enter an adjective :")
place=input("Enter a place: ")
emotion=input("enter an emotional feeling: ")
animal=input("Enter an animal :")
weather=input("What's weather like today ,(Sunny, Windy,cloudy,Rainy, snowy, etc.. ?:)")

if weather.lower()=="rainy":
    weather_activity="Jumped in muddy puddles."
elif weather.lower() =="sunny":
    weather_activity="went for a long walk and soaked the sunshine."
elif weather.lower()=="snowy":
    weather_activity="built a snowman and had a snowball fight."
elif weather.lower()=="cloudy":
    weather_activity="Predict the rain or sun in the next hour."
else:
    weather_activity="decided to stay indoors and read some books."

    #The story part 
story=f"""
one {weather} day, {name} was walking through the  {place}, with a {adjective} {animal}.
suddenly, they found a {noun} lying on the ground. curious, {name} picked it up and decided to {verb} with it.
they felt very {emotion} about the whole situation.
to make the most of the day, {name} and the animal {weather_activity}.
it was a fun day to remember!

"""
    # displaying the final story

print ("/n Here is your mad lib story!!!!")
print(story)

