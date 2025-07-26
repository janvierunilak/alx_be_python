class point :
    def _init_(self,x,y):
        self.x=x
        self.y=y
def where_is(point):
    match point:
        case point(x=0,y=0):
            print("Origin !")
        case point(x=0,y=y):
            print(f"Y= {y}")
        case point(x=x,y=0):
            print(f" X= {x} ") 
        case point():
            print("Nothing")
        case _ :
            print("Unexpected error, not a point")         
                                   
