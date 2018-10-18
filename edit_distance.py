
def getDist(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1

    mTable = {}
    for i in range(0,m):
        for j in range (0,n):
            mTable[i,j] = 0

    for i in range(0, m):
        mTable[i, 0] = i

    for i in range(0, n):
        mTable[0, i] = i

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            mTable[i,j] =  min([mTable[i, j - 1] + 1, mTable[i - 1, j] + 1, mTable[i - 1, j - 1] + cost])

    #printing the table

    print("     ", end='')
    for j in range(0, n - 1):
        print("| " + s2[j] + " ", end='')
    print("\n")
    for i in range(0, m - 1):
        if i == 0:
            print("     ", end='')
        if i > 0:
            print(" " + s1[i - 1] + " ", end='')
        for j in range(0, n):
            print("| " + str(mTable[i,j]) + " ", end='')
        print("\n")


    return mTable, mTable[m -1, n - 1]


if __name__ == '__main__':
    sString1 = "vintner"
    sString2 = "writers"

    mTable, editDistance = getDist(sString1,sString2)
    print(editDistance)