def bondify():
    name = input("Enter your first and last name:")
    if(name == ""):
        name = "James Bond"
    lastName = name.split(" ")[1]
    bondified = lastName + ", " + name
    print(bondified)
    return bondified


bondify()
