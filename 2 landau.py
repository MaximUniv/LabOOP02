str1 = "abcd"
str2 = "abc"

def isSubRow(str1, str2):
    no = 0
    counter = 0
    indexOfElement = 0
    if ((len(str1) - len(str2)) > 1):
        return "No"
    if (len(str1) < len(str2)):
        return "str2 is bigger than str1"

    if ((len(str1) == len(str2)) and (str1[0] != str2[0]) and (str1[len(str1)-1] != str2[len(str2)-1]) ):
        return "No"


    for i in range(0, len(str1)):
        if(str1[i] == str2[0]):
            indexOfElement = i
        for i in range(0, len(str2)):

            if(str1[indexOfElement] != str2[i] and counter < 1 and len(str1) != len(str2)):
                counter += 1
                indexOfElement += 1
                no = "Yes"

            if (str1[indexOfElement] != str2[i] and counter < 1):
                counter += 1
                indexOfElement += 1
                no = "Yes"
            else:
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


