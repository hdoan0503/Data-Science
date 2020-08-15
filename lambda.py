#normal function
def dou(var):
    return var*2
#to lambda function
t = lambda var: var*2

#map()
seq = [1, 2, 3, 4, 5]
print(list(map(lambda item: item*3, seq)))


#filter
#get the even number inside a list
print(list(filter(lambda num: num%2 == 0, seq)))





