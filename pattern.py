def pattern(n):
    # Number of spaces
    a = (2 * n) - 2
    for i in range(n, -1, -1):
        for j in range (a, 0, -1):
            print(end=" ")
        
        #incrementing a after each loop
        a = a + 1
        for j in range (0, i+1):
            #printing stars
            print("* ",end=" ")
        print("\r")

# take inputs
n = int(input("Enter the number of rows: "))      

#calling function
pattern(n)