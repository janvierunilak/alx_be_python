shopping_list=["apples","carrots","onions","cabbages","watermellon","rice","bread","liquor","wine"]
item_found=False

while not item_found:
    item=input("enter item to search or press ('q' to quit:): ")
    if item.lower()=='q':
        break
    if item in shopping_list:
        item_found=True
        print(f" {item}  found successfully !!!")
    else:
        print(f"{item} not found , try again! >:")
        
