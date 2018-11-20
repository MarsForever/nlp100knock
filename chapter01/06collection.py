target1 = "paraparaparadise"
target2 = "paragraph"
result1 = set()
result2 = set()

num1 = 0
num2 = 0
for x in range (len(target1)-1):
    result1.add(target1[num1:num1+2])
    num1 += 1

for y in range (len(target2)-1):
    result2.add(target2[num2:num2+2])
    num2 += 1
# XとYとして求め
print(result1)
print(result2)

#XとYの和集合，積集合，差集合を求めよ
print(" X U Y = ",result1.union(result2))
print(" X ∩ Y = ",result1.intersection(result2))
#symmetric_difference or ^
print(" X ∆ Y = ",(result1.symmetric_difference(result2)))

#'se'というbi-gramがXおよびYに含まれるかどうかを調べよ
if 'se' in result1:
    print("se in X")
else:
    print("se not in X")

if 'se' in result2:
    print("se in Y")
else:
    print("se not in Y")
    