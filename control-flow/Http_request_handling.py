def http_error(status):
    match status :
        case 400|404|401|402:
            print("Bad request")
        case 200:
            print("Successfully")
        case 418:
            print("Bad gateway")
        case _ :
            print("Something wrong with the internet <:> ") 

http_error(2000)                   