target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word = target.replace(",","")
word = word.replace(".","")
word = word.split(" ")
ret =[]
for a in word:
    ret.append(len(a))
print(ret)

