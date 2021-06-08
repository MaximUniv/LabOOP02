def isSubSequence(str1, str2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False

    if str1[m - 1] == str2[n - 1]:
        return isSubSequence(str1, str2, m - 1, n - 1)

    return isSubSequence(str1, str2, m, n - 1)


str1 = "abcd"
str2 = "a-b-c-d"

if isSubSequence(str1, str2, len(str1), len(str2)):
    print("Yes")
else:
    print("No")
