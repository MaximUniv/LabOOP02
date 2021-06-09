str1 = "abcd"
str2 = "aba"

def isSubRow(str1, str2):
    no = 0
    for i in range(0, len(str1)):
        if(str1[i] == str2[0]):
            indexOfElement = i
        for i in range(0, len(str2)):
            if(str1[indexOfElement] == str2[i]):
                indexOfElement += 1
                no = "Yes"
            else:
                no = 0
                break
        if (no == "Yes"):
            return "Yes"
    return "No"

print(isSubRow(str1, str2))


