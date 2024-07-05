def double(x):
    return x * 2

def getName(name):
    return name

def filterList(list, filterkey):
    #the lambda expression checks if the x is equals the current element in the list
    return filter(lambda x: x == filterkey, list)
#lambda expressions use variables and returns the result of expressions with the variable in use

#this lambda uses the x parameter and returns the x2 of the x, x = x * 2
mylambda = lambda x: double(x) * 2
#this lambda uses name and greets the name, (name) = hello {name}
grtLambda = lambda name: "hello " + getName(name)

#TESTING AREA
print(list(filterList([1,1,4,5,4,7,5], 4)))
