#You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

#The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

#From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

#count the number of trees on route 

#read in data from text file

#column length

with open('advocd3data.txt', 'r') as f:
    lines = f.read().splitlines()
    

print(lines)

# print(rows[1][3])
# print(rows[2][6])
# print(rows[3][9])
# print(rows[4][1])
# print(rows[5][4])

row = 1
col = 3
numOfRows = len(lines)
lenOfRow = len(lines[0])
print("lenofRow:")
print(lenOfRow)
treeCount = 0

for line in lines:
    if col >= lenOfRow:
        col = col%lenOfRow
    print(row)
    print(col)
    if row < numOfRows:
        print(lines[row][col])    
        if lines[row][col] == "#":
            treeCount += 1

    row +=1
    col +=3   

print("treeCount:")    
print(treeCount)