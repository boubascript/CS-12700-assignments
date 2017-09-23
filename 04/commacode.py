def commaList(list):
    result = ""
    for l in list:
        if list.index(l) == len(list) - 1:
            next = "and " + l + "."
        else:
            next = l + ", "
        result += next
    return result


testlist = ["Bulbasaur", "Ivysaur" , "Charmander" , "Charmeleon" , "Charizard", "Squirtle", "Wartortle"]
print(commaList(testlist))