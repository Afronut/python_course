

b=[1,2,3,4,5,6,6,6,5,5, 10]

total=0
for el in b:
    total=total+el

# print(total)

c=[11,2,14,8,16,20,40,7,94,19]

plus_grand=None
for el in c:
    if plus_grand==None or plus_grand <el :
        plus_grand=el
print(plus_grand)