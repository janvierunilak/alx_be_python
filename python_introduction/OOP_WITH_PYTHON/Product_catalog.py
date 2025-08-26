class product_catalog:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

        

    def stock_value(self,Total_price):
        Total_price={price1.price * price1.quantity}
        return Total_price

price1=product_catalog("Ginger", 122,100)  

print(f"The {price1.name} has a price of $ {price1.price} with a stock of {price1.quantity} kg") 
print(f" The total Amount is {price1.stock_value(Total_price=price1.price * price1.quantity)}")