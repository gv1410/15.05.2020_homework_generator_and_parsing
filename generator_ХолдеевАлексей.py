

def my_gen():
    a = 0

    while a < 25:
        if a % 3 == 0:
            yield 'Вася'
        else:
            yield a
        
        a += 1
  
for i in my_gen():
    print(i)

'''
g = my_gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''