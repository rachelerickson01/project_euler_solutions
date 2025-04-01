# Multiples of 3 or 5
mysum = 0
exclude = []
for i in range(1000):
    if i%3==0:
        mysum+=i
    elif i%5==0:
        mysum+=i
print(mysum)