result = []
def divider(a, b):
    if a < b:
        raise ValueError()
    if b > 100:
        raise IndexError()
    if b == 0:
        raise ZeroDivisionError()
    return a/b
data = {10 : 2, 2 : 5, 123 : 4, 18 : 1, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except :
        print("Nepravilno")

print(result)