def listanalisis(num6,num7,num8,num9,num10):
    num6= int(input("enter number: "))
    num7= int(input("enter number: "))
    num8= int(input("enter number: "))
    num9= int(input("enter number: "))
    num10= int(input("enter number: "))
    lists=[num6,num7,num8,num9,num10]
    print("YOUR LIST IS " )
    print(lists)
    highest_number = max(lists)
    minimum_number = min(lists)
    print(highest_number)
    print(minimum_number)
    print(len(lists))
    
    
listanalisis("num6","num7","num8","num9","num10")
