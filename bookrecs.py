""" Tyson Elfors
5/21/20
CS-1410
Project 2 
"""

#module variables  
bookArr = []
readerObj = {}

readerArr = [] #temp var for converting to dict

#Read file into list and dict
with open('booklist.txt') as allBooks:
    for line in allBooks:
        stripped = line.strip('\n')
        splitLines = tuple(stripped.split(","))
        bookArr.append(splitLines)
with open('ratings.txt') as allRatings:
    for line in allRatings:
        stripped = line.strip('\n')
        readerArr.append(stripped)
    it = iter(readerArr)
    res_dct = dict(zip(it, it))
listOfStrsDict = dict((k, list(v.split(" "))) for k,v in res_dct.items())
removeSpacesDict = dict((k.lower(), list(filter(None, v))) for k,v in listOfStrsDict.items())
listIntDict = dict((k, [int(s) for s in v]) for k,v in removeSpacesDict.items())
readerObj = listIntDict

#How to calculate the dot product
def addDotProd(arr1, arr2):
    resList = []
    total = 0
    for i in range(0, len(arr1)):
        resList.append(arr1[i] * arr2[i])
    for i in resList:
        total += i
    return total  

#Recommend books based on two best friends
def recommend(friendList, person):
    print(f"{person}'s best friends : ", friendList) #print the two best friends
    
    pers = person

    fOne = friendList[0]
    fTwo = friendList[1]

    persDots = readerObj.get(pers)
    fOneDots = readerObj.get(fOne)
    fTwoDots = readerObj.get(fTwo)

    zipped = zip(fOneDots, fTwoDots)
    zippedList = list(zipped)
    
    maxOfFriendDots = []
    for tup in zippedList:
        maxOfFriendDots.append(max(tup)) 

    zippedTotal = list(zip(maxOfFriendDots, persDots))
    iterator = 1
    for tup in zippedTotal:
        if tup[0] >= 3 and tup[1] == 0:
            newVal = zippedTotal.index(tup)
            zippedTotal[newVal] = iterator
            iterator += 1

    iterate = 1
    listOfIndexes = []
    for tup in zippedTotal:
        if tup == iterate:
            listOfIndexes.append(zippedTotal.index(tup)) 
            iterate += 1

    listOfBooks = []
    for i in listOfIndexes:
        listOfBooks.append(bookArr[i])
    print(f"Recommended books for {person} : ", listOfBooks) #print the recommended books

#Create a list of the two best friends
def friends(arrOfDotProds, person):
    listOfReaderObj = list(readerObj.keys())

    result = list(zip(arrOfDotProds, listOfReaderObj))
    newRes = list(filter(lambda x: x[1] != person, result))
    newRes.sort(key=lambda x: x[0])
    
    friendList = []
    friendOne = newRes[-1][1]
    friendTwo = newRes[-2][1]
    friendList.append(friendOne)
    friendList.append(friendTwo)
    friendList.sort()

    recommend(friendList, person)
    
#initialize person to find dot prod
def dotProd(person):
    initialValue = readerObj.get(person)

    dotProds = []
    for k,v in readerObj.items():
        res = addDotProd(initialValue, v)
        dotProds.append(res)
    friends(dotProds, person)


def main():
    """ This is a program computes book recommendations for readers based on other readers
    with similar tastes in books. 
    """
    initialPerson = input("Who would you like to find recommendations for? : ") 
    availablePeople = list(readerObj.keys())   
    if initialPerson in availablePeople:
        dotProd(initialPerson)  #call function with person name
    else:
        print('Reader not found, try again')
    
main()