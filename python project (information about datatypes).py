

while True:
    print("MAIN MENU\n1.List\n2.Tuple\n3.Set\n4.Dictionary\n5.Exit")
    menuch = int(input("Enter your choice:"))
    # list
    if menuch == 1:
        while True:
            print(
                "LIST OPERATIONS\n1.Defination\n2.Addition\n3.Deletion\n4.Previous Menu"
            )
            listch = int(input("Enter your choice:"))
            if listch == 1:
                print(
                    "List is a ordered collection of heterogeneous elements which are mutable."
                )
            # list addition
            elif listch == 2:
                lst = []
                n = int(input("Enter the total number of elements to create list:"))
                for i in range(0, n):
                    ele = input("Enter elements to create list:")
                    lst.append(ele)
                print("------------------------------")
                print(lst)
                print("------------------------------")
                while True:
                    print(
                        "1.To add single element.\n2.To add multiple elements.\n3.To add element at specific index position.\n4.Previous Menu"
                    )
                    addch = int(input("Enter your choice:"))
                    if addch == 1:
                        element = input("Enter element to add:")
                        lst.append(element)
                        print("------------------------------")
                        print(lst)
                        print("------------------------------")
                    elif addch == 2:
                        lst2 = []
                        elements = int(input("Enter number of elements to add:"))
                        for i in range(0, elements):
                            element = input("Enter Element to add:")
                            lst2.append(element)
                        lst.extend(lst2)
                        print("------------------------------")
                        print(lst)
                        print("------------------------------")
                    elif addch == 3:
                        pos = int(input("Enter the index position to add element:"))
                        val = input("Enter Element to add:")
                        lst.insert(pos, val)
                        print("------------------------------")
                        print(lst)
                        print("------------------------------")
                    elif addch == 4:
                        break
                    else:
                        print("Invalid Input")
            # list deletion
            elif listch == 3:
                lst = []
                n = int(input("Enter the total number of elements to create list:"))
                for i in range(0, n):
                    ele = input("Enter list elements:")
                    lst.append(ele)
                print("------------------------------")
                print(lst)
                print("------------------------------")
                while True:
                    print(
                        "1.To delete last element.\n2.To delete element by index position.\n3.To delete element by value\n4.Previous Menu"
                    )
                    delch = int(input("Enter your choice:"))
                    if delch == 1:
                        lst.pop()
                        print("------------------------------")
                        print(lst)
                        print("------------------------------")
                    elif delch == 2:
                        pos = int(input("Enter index position to delete element:"))
                        lst.pop(pos)
                        print("------------------------------")
                        print(lst)
                        print("------------------------------")
                    elif delch == 3:
                        element = input("Enter element to delete:")
                        lst.remove(element)
                        print("------------------------------")
                        print(lst)
                        print("------------------------------")
                    elif delch == 4:
                        break
                    else:
                        print("Invalid Input")
            elif listch == 4:
                break
            else:
                print("Invalid Input")
    # tuple
    elif menuch == 2:
        while True:
            print(
                "TUPLE OPERATIONS\n1.Defination.\n2.Addition.\n3.Deletion\n4.Previous Menu"
            )
            tplch = int(input("Enter your choice:"))
            if tplch == 1:
                print(
                    "Tuple is a ordered collection of heterogeneous elements which are Immutable."
                )
            # tuple addition
            elif tplch == 2:
                tpl = ()
                n = int(input("Enter the total number of elements to create tuple:"))
                lst = list(tpl)
                for i in range(0, n):
                    ele = input("Enter elements to create tuple:")
                    lst.append(ele)
                tpl = tuple(lst)
                print("------------------------------")
                print(tpl)
                print("------------------------------")
                while True:
                    print(
                        "1.To add single element.\n2.To add multiple elements.\n3.To add element at specific index position.\n4.Previous Menu"
                    )
                    addch = int(input("Enter your choice:"))
                    lst = list(tpl)
                    if addch == 1:
                        element = input("Enter element to add:")
                        lst.append(element)
                        tpl = tuple(lst)
                        print("------------------------------")
                        print(tpl)
                        print("------------------------------")
                    elif addch == 2:
                        lst2 = []
                        elements = int(input("Enter number of elements to add:"))
                        for i in range(0, elements):
                            element = input("Enter Element to add:")
                            lst2.append(element)
                        lst.extend(lst2)
                        tpl = tuple(lst)
                        print("------------------------------")
                        print(tpl)
                        print("------------------------------")
                    elif addch == 3:
                        pos = int(input("Enter the index position to add element:"))
                        val = input("Enter Element to add:")
                        lst.insert(pos, val)
                        tpl = tuple(lst)
                        print("------------------------------")
                        print(tpl)
                        print("------------------------------")
                    elif addch == 4:
                        break
                    else:
                        print("Invalid Input")
            # tuple deletion
            elif tplch == 3:
                tpl = ()
                n = int(input("Enter the total number of elements to create tuple:"))
                lst = list(tpl)
                for i in range(0, n):
                    ele = input("Enter elements to create tuple:")
                    lst.append(ele)
                tpl = tuple(lst)
                print("------------------------------")
                print(tpl)
                print("------------------------------")
                while True:
                    print(
                        "1.To delete last element.\n2.To delete element by index position.\n3.To delete element by value\n4.Previous Menu"
                    )
                    delch = int(input("Enter your choice:"))
                    lst = list(tpl)
                    if delch == 1:
                        lst.pop()
                        tpl = tuple(lst)
                        print("------------------------------")
                        print(tpl)
                        print("------------------------------")
                    elif delch == 2:
                        pos = int(input("Enter index position to delete element:"))
                        lst.pop(pos)
                        tpl = tuple(lst)
                        print("------------------------------")
                        print(tpl)
                        print("------------------------------")
                    elif delch == 3:
                        element = input("Enter element to delete:")
                        lst.remove(element)
                        tpl = tuple(lst)
                        print("------------------------------")
                        print(tpl)
                        print("------------------------------")
                    elif delch == 4:
                        break
                    else:
                        print("Invalid Input")
            elif tplch == 4:
                break
            else:
                print("Invalid Input")
    # set
    elif menuch == 3:
        while True:
            print(
                "SET OPERATIONS\n1.Defination.\n2.Addition.\n3.Deletion\n4.Previous Menu"
            )
            setch = int(input("Enter your choice:"))
            if setch == 1:
                print(
                    "Set is unordered collection of homogeneous elements which are mutable."
                )
            # set addition
            elif setch == 2:
                sett = set()
                n = int(input("Enter the total number of elements to create set:"))
                for i in range(0, n):
                    ele = input("Enter elements to create set:")
                    sett.add(ele)
                print("------------------------------")
                print(sett)
                print("------------------------------")
                while True:
                    print(
                        "1.To add single element.\n2.To add multiple elements.\n3.Previous Menu"
                    )
                    addch = int(input("Enter your choice:"))
                    if addch == 1:
                        element = input("Enter element to add:")
                        sett.add(element)
                        print("------------------------------")
                        print(sett)
                        print("------------------------------")
                    elif addch == 2:
                        elements = int(input("Enter number of elements to add:"))
                        for i in range(0, elements):
                            element = input("Enter Element to add:")
                            sett.add(element)
                        print("------------------------------")
                        print(sett)
                        print("------------------------------")
                    elif addch == 3:
                        break
                    else:
                        print("Invalid Input")
            # set deletion
            elif setch == 3:
                sett = set()
                n = int(input("Enter the total number of elements to create set:"))
                for i in range(0, n):
                    ele = input("Enter elements to create set:")
                    sett.add(ele)
                print("------------------------------")
                print(sett)
                print("------------------------------")
                while True:
                    print(
                        "1.To delete random element.\n2.To delete element by value.\n3.Previous Menu"
                    )
                    delch = int(input("Enter your choice:"))
                    if delch == 1:
                        sett.pop()
                        print("------------------------------")
                        print(sett)
                        print("------------------------------")
                    elif delch == 2:
                        element = input("Enter element to delete:")
                        sett.discard(element)
                        print("------------------------------")
                        print(sett)
                        print("------------------------------")
                    elif delch == 3:
                        break
                    else:
                        print("Invalid Input")
            elif setch == 4:
                break
            else:
                print("Invalid Input")
    # dictionary
    elif menuch == 4:
        while True:
            print(
                "SET OPERATIONS\n1.Defination.\n2.Addition.\n3.Update.\n4.Deletion.\n5.Previous Menu"
            )
            dictch = int(input("Enter your choice:"))
            if dictch == 1:
                print(
                    "Dictionary is unordered collection of heterogeneous elements which are mutable."
                )
            # dictionary addition
            elif dictch == 2:
                dict = {}
                n = int(
                    input(
                        "Enter the total number of key value pairs to create dictionary:"
                    )
                )
                for i in range(0, n):
                    key = input("Enter key to create dictionary:")
                    value = input("Enter value to create dictionary:")
                    dict[key] = value
                print("------------------------------")
                print(dict)
                print("------------------------------")
                elements = int(input("Enter number of key value pairs to add:"))
                for i in range(0, elements):
                    key = input("Enter key to add in dictionary:")
                    value = input("Enter value to add in dictionary:")
                    dict[key] = value
                print("------------------------------")
                print(dict)
                print("------------------------------")
            # dictionary update
            elif dictch == 3:
                dict = {}
                n = int(
                    input(
                        "Enter the total number of key value pairs to create dictionary:"
                    )
                )
                for i in range(0, n):
                    key = input("Enter key to create dictionary:")
                    value = input("Enter value to create dictionary:")
                    dict[key] = value
                print("------------------------------")
                print(dict)
                print("------------------------------")
                elements = int(input("Enter number of key value pairs to update:"))
                for i in range(0, elements):
                    key = input("Enter key to update in dictionary:")
                    value = input("Enter value to update in dictionary:")
                    dict[key] = value
                print("------------------------------")
                print(dict)
                print("------------------------------")
            # dictionary deletion
            elif dictch == 4:
                dict = {}
                n = int(
                    input(
                        "Enter the total number of key value pairs to create dictionary:"
                    )
                )
                for i in range(0, n):
                    key = input("Enter key to create dictionary:")
                    value = input("Enter value to create dictionary:")
                    dict[key] = value
                print("------------------------------")
                print(dict)
                print("------------------------------")
                elements = int(input("Enter number of key value pairs to delete:"))
                for i in range(0, elements):
                    key = input("Enter key to delete in dictionary:")
                    dict.pop(key)
                print("------------------------------")
                print(dict)
                print("------------------------------")
            elif dictch == 5:
                break
            else:
                print("Invalid Input")
    elif menuch == 5:
        break
    else:
        print("Invalid Input")





