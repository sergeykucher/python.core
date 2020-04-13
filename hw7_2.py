def list_animals(animals):
    list1 = ''
    for i in range(len(animals)):
        list1 += str(i + 1) + '. ' + animals[i] + '\n'
    return list1