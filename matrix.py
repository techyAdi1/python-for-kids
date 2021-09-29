shnum = int(input("Enter a number: "))
for i in range(shnum):
    for j in range(shnum):
        if i == 0 or i == shnum-1 or j == 0 or j == shnum-1 or i == j:
            print("* " , end="")
        else:
            print("  ",end='')
    print('')       
