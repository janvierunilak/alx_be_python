class Animals:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        return "Barking Wooof !"
dog1=Animals("Muddy","Italian")
dog2=Animals("MAX","German shepherd")
print(f" the DOg {dog1.name} is an {dog1.breed} and speaks by { dog1.bark()}")
print(f" The Dog {dog2.name} is a {dog2.breed} and speaks by {dog2.bark()}")
    

    