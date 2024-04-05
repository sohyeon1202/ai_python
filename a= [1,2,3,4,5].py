a= [1,2,3,4,5]
tot = 0
for i in a:
    print(i)
    tot+=i
print(tot)

for i in range(1,11):
    print(i)

for i in range(2, 101, 2):
    print(i)

for i in range(1,101):
    if i%2 == 1:
        continue
    print(i)