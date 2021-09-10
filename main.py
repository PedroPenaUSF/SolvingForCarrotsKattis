# Step 1 Receive user input
str1 = input()

# Step 2 separate the inputs by the ' ' value
str1 = str1.split(' ')

# Step 3 first number is contestants and amount of loop, second number is amount of carrots given and our output.

n = int(str1[0])
o = int(str1[1])

# Step 4 run loop to accept user input, however input does not need to be stored
for i in range(n):
    input()

# step 5 print second element after split.
print(o)
