# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.

# def keyword is used to create function

def oddNumber():
    l = []
    for i in range(1, 26, 2):  
        l.append(i)
    return l

print(oddNumber())

lsit=[2,4,5,6,8,6,8,4]
print(list(filter(lambda x:x%2==0, lsit)))