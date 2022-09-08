lst=[]
while True:
    name=input("Enter Name\n")
    if name.lower() in lst:
        print("already exist")
        break;
    else:
        lst.append(name.lower())

