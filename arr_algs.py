
mass =  [7, 3, 5, 2, 6]
#минимум
def min(mass):
    a = mass[0]
    for i in mass:
        if i < a:
            a = i
    return a
print(mass)
print(min(mass))

#среднее

def mean(mass):
    r = 0
    for i in mass:
        r += i
    return r/len(mass)

print(mean(mass))