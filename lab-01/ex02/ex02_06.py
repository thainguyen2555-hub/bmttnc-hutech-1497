input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(",")]
rowNUM=dimensions[0]
colNUM=dimensions[1]
multilist = [[0 for col in range(colNUM)] for row in range(rowNUM)]
for row in range(rowNUM):
    for col in range(colNUM):
        multilist[row][col] = row * col
print(multilist)