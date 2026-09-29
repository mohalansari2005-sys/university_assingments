

def program1():
    # Part A: collect item costs in a list until the user enters -1.
    cost = float(input("please enter the cost of the item or -1 to stop: "))
    listOfCost = []

    while cost != -1:
        listOfCost.append(cost)
        cost = float(input("please enter the cost of the item or -1 to stop: "))

    if not listOfCost:
        print("No costs were entered.")
        return

    # B1: display the list of costs.
    print(f"The cost list: {listOfCost}")

    # B2: display the number of elements in the list.
    numberOfElements = len(listOfCost)
    print(f"The number of elements in the list: {numberOfElements}")

    # B3: display the highest cost in the list.
    highestCost = max(listOfCost)
    print(f"The highest cost in the list: {highestCost}")

    # B4: display the lowest cost in the list.
    lowestCost = min(listOfCost)
    print(f"The lowest cost in the list: {lowestCost}")

    # B5: display the total of the costs in the list.
    totalCosts = 0
    for n in listOfCost:
        totalCosts += n
    print(f"The total of the costs in the list: {totalCosts}")

    # B6: display the average of the costs in the list.
    avgCosts = totalCosts / len(listOfCost)
    print(f"The average of the costs: {avgCosts}")

    # B7: change the value at index 5 to 40 and display the result.
    if len(listOfCost) > 5:
        listOfCost[5] = 40
        print(f"The value at index 5 after changing it to 40: {listOfCost[5]}")
    else:
        print("There is no value at index 5 to change.")

    # B8: remove the fourth cost and display the list before and after deletion.
    if len(listOfCost) >= 4:
        print(f"List before deleting the fourth cost: {listOfCost}")
        del listOfCost[3]
        print(f"List after deleting the fourth cost: {listOfCost}")
    else:
        print("The list does not have a fourth cost to delete.")

    # B9: remove the first occurrence of 48, or display a message if it is absent.
    if 48 in listOfCost:
        listOfCost.remove(48)
        print(f"The first occurrence of 48 was removed: {listOfCost}")
    else:
        print("48 was not found in the list.")

    # C 
    tupleOfCosts = listOfCost.tuple()
    
    
def program2():
    
    table =[]
    for _ in range(2):
        c1 = input(" enter the first char: ")
        c2 = input(" enter the second char: ")
        c3 = input(" enter the third char: ")
        
        row = [c1, c2 , c3]
        table.append(row)
        
    for row in table:
        slicedList = table[:2]
        print(slicedList)
        
    
    newList = [[0, 0, 0],
               [0, 0, 0]]   
    
    for i in range(2):
        for j in range(3):
            newList[i][j] = table[j][i]
         
        
    
    
    

def program3():
    # Ask the user for a word and the number of copies.
    word = input("Enter word: ")
    copies = int(input("Enter the number of copies: "))

    # Print the word the square of the requested number of copies.
    numberOfCopies = copies ** 2
    print(" ".join([word] * numberOfCopies))


def program4():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if len(string1) != len(string2):
        print("False")
        return

    sameCharacters = True
    sortedString1 = sorted(string1)
    sortedString2 = sorted(string2)

    for index in range(len(string1)):
        if sortedString1[index] != sortedString2[index]:
            sameCharacters = False
            break

    print("Yes" if sameCharacters else "False")


def program5():
    stringList = input("Enter the string list, separated by commas: ").split(",")
    removeList = input("Enter the remove list, separated by commas: ").split(",")
    resultList = []

    for sentence in stringList:
        filteredSentence = []
        for currentWord in sentence.strip().split():
            shouldRemove = False
            for removeWord in removeList:
                if removeWord.strip() in currentWord:
                    shouldRemove = True
                    break
            if not shouldRemove:
                filteredSentence.append(currentWord)
        resultList.append(" ".join(filteredSentence))

    print(f"String list: {stringList}")
    print(f"Remove list: {removeList}")
    print(f"Result list: {resultList}")






