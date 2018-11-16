
# coding= shift_jis


target = u"パタトクカシーー"
# print(target[::2])
res = u""

for i in range(1, len(target) - 1, 2):
	res += target[i]

print(res)