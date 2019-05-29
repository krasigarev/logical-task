town = input()
s = float(input())

if town == 'Sofia':
    if s >= 0 and s <= 500:
        result = s * 0.05
    elif s > 500 and s <= 1000:
        result = s * 0.07
    elif s > 1000 and s <= 10000:
        result = s * 0.08
    elif s > 10000:
        result = s * 0.12
elif town == 'Plovdiv':
    if s >= 0 and s <= 500:
        result = s * 0.055
    elif s > 500 and s <= 1000:
        result = s * 0.08
    elif s > 1000 and s <= 10000:
        result = s * 0.12
    elif s > 10000:
        result = s * 0.135

elif town == 'Varna':
    if s >= 0 and s <= 500:
        result = s * 0.045
    elif s > 500 and s <= 1000:
        result = s * 0.075
    elif s > 1000 and s <= 10000:
        result = s * 0.1
    elif s > 10000:
        result = s * 0.13

else:
    result = 'error'

if type(result) == str:
    print(result)

else:
    print("{0:.2f}".format(result))
