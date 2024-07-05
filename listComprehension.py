#list comprehension is adding elements in a list with a condition

#this method turns a camel or pascal cased string to snake case

def snake_caser(stringItem):
    #in list comprehension, you add the if else first before iterating
    snake_cased_list = ['_' + char.lower() if char.isupper() else char for char in stringItem]
    #you join the list to form a string
    result = ''.join(snake_cased_list)
    #the result will stripped of excess _ at the beginning or its end
    return result.strip('_')

print(snake_caser('iAmPhilipJohn'))

