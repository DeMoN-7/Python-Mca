# program to read csv and return a 2d list

fileName = "data1.csv"


def read_csv(fileName):

    fileHandle = open(fileName, "r")
    data = fileHandle.read()
    fileHandle.close()
    # returnData = data
    # data.strip("")
    rows = data.split("\n")
    for i in range(0,len(rows)):
        row=rows[i]
        rows[i]=row.split(",")
    op=rows
    return op


list1 = read_csv(fileName)
print(list1[1])
