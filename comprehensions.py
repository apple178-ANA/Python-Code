temp = [30,28,40,35]
farhen = [item*(9/5)+32 for item in temp]
print(farhen)
square = [item**2 for item in range(3)]
print(square)
evens = [item for item in range(10)if item %2== 0]
print (evens)
squaremap = {item: item**2 for item in range(6)}
print (squaremap)
unique_initials ={item[0].lower() for item in ["Asha","apple","banana"]}
print (unique_initials)


