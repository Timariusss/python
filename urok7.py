'''
my_list = [1, 2, 3]
iterator = iter(my_list)
print(iterator)


print(next(iterator))
print(next(iterator))
print(next(iterator)) 
print(next(iterator))  

for elem in iterator:
    print(elem)

class Counter:
    def __init__(self,max_number): 
        self.i = 0 
        return self 
    
    def __next__(self):
        if self.i > self.max_number: 
            raise StopIteration
        return self.i
count = Counter(5)

for elem in count:
    print (elem)
'''
def squares(n):
    for i in range(n):
        yield i**2

for num in squares(5):
    print(num)

# generator 

def raise_to_degrees(number, max_degree):
    i = 0 
    for _ in range(max_degree):
        yield number ** i 
    i += i
res = raise_to_degrees(2,5)
for value in res:
    print(value)


def counter():
    count = 0 

    def increase():
        nonlocal count 
        count += 1 
        return count 
    return increase 

c = counter 

print(c())
print(c())
print(c())
print(c())