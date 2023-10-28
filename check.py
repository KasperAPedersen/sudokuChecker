import os
os.system('cls')
tmpArr = [[],[],[],[],[],[],[],[],[]]
testValues = [
    ["295743861","431865927","876192543","387459216","612387495","549216738","763524189","928671354","154938672"],
    ["195743862","431865927","876192543","387459216","612387495","549216738","763524189","928671354","254938671"]
]

def av(index, valueIndex):
    return tmpArr[index][valueIndex]

def check(arr):
    for row in enumerate(arr):
        for v in enumerate(row[1]):
            tmpArr[row[0]].append(v[1])

    # Checking if every row is filled correctly
    for row in enumerate(tmpArr):
        correctRow = True
        for i in range(9):
            try:
                if tmpArr[row[0]].index(str(i + 1)): continue
            except:
                correctRow = False
                break
        if not correctRow: return False

    # Checking if every coloum is filled correctly
    for i in range(9):
        correctColoum = True
        newStr = ""
        for row in enumerate(tmpArr): newStr += row[1][i]
        for cV in range(9):
            try:
                if newStr.find(str(cV + 1)): continue
            except:
                correctColoum = False
                break
        if not correctColoum: return False
    

    # Checking if every square is filled correctly
    newArr = [ # sort array so each array element is equal to 1 square
        [ av(0,0), av(0,1), av(0,2), av(1,0), av(1,1), av(1,2), av(2,0), av(2,1), av(2,2) ], # TL
        [ av(0,3), av(0,4), av(0,5), av(1,3), av(1,4), av(1,5), av(2,3), av(2,4), av(2,5) ], # TM
        [ av(0,6), av(0,7), av(0,8), av(1,6), av(1,7), av(1,8), av(2,6), av(2,7), av(2,8) ], # TR

        [ av(3,0), av(3,1), av(3,2), av(4,0), av(4,1), av(4,2), av(5,0), av(5,1), av(5,2) ], # ML
        [ av(3,3), av(3,4), av(3,5), av(4,3), av(4,4), av(4,5), av(5,3), av(5,4), av(5,5) ], # MM
        [ av(3,6), av(3,7), av(3,8), av(4,6), av(4,7), av(4,8), av(5,6), av(5,7), av(5,8) ], # MR

        [ av(6,0), av(6,1), av(6,2), av(7,0), av(7,1), av(7,2), av(8,0), av(8,1), av(8,2) ], # BL
        [ av(6,3), av(6,4), av(6,5), av(7,3), av(7,4), av(7,5), av(8,3), av(8,4), av(8,5) ], # BM
        [ av(6,6), av(6,7), av(6,8), av(7,6), av(7,7), av(7,8), av(8,6), av(8,7), av(8,8) ] # BR
    ]
    
    for i in enumerate(newArr): # Loop through each array element of newArr
        correctSquare = True
        for n in range(9): # Loop 9 times
            try:
                if i[1].index(str(n + 1)): continue # If array element has loop n Index in it, continue
            except: # If an error occoured,
                correctSquare = False # set correctSquare to false
                break # & break loop
        if not correctSquare: return False # if correctSquare is false, return with false

    # All checks has been succesful
    return True # return true
            
    
while True:
    tmpArr = [[],[],[],[],[],[],[],[],[]]
    print("Test values available!", end="\n")
    for elem in enumerate(testValues): print("[" + str(elem[0]) + "] " + str(elem[1]), end="\n")
    uInput = int(input("Select which test values to try: "))
    if int(uInput) >= 0 and int(uInput) <= len(testValues): print("Yes" if check(testValues[uInput]) else "No", end="\n\n\n")

# 2 9 5 | 7 4 3 | 8 6 1
# 4 3 1 | 8 6 5 | 9 2 7
# 8 7 6 | 1 9 2 | 5 4 3

# 3 8 7 | 4 5 9 | 2 1 6
# 6 1 2 | 3 8 7 | 4 9 5
# 5 4 9 | 2 1 6 | 7 3 8

# 7 6 3 | 5 2 4 | 1 8 9
# 9 2 8 | 6 7 1 | 3 5 4
# 1 5 4 | 9 3 8 | 6 7 2