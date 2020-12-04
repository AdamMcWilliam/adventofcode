#You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

#The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

#From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

#count the number of trees on route 

#read in data from text file

#column length
cLength = 30
col = 0
treeCount = 0


with open('2020/advocd3data.txt', 'r') as f:
    for line in f:
        row = line.split() 

        #move right 3 
        col +=3
        if col > cLength:
            col = int(repr(col)[-1])

        #go down 1
        row = f.readline()
        if row !="":
            print(row)
            print(col)
            rowData = row[col]
            #print (rowData)
            #check for tree
            if rowData == "#":
                treeCount += 1
                
print(treeCount)
        
