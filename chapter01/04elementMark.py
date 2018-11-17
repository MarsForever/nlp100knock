target = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = target.replace(".","")
words = words.split(" ")
data={}
num = 0
for x in words:
    if num == 0 or \
       num == 4 or \
       num == 5 or \
       num == 6 or \
       num == 7 or \
       num == 8 or \
       num == 14 or \
       num == 15 or \
       num == 18:
        data[x[0]] = num
        print(x)
    else:
        data[x[0:2]] = num
        print(x)
    num += 1
print(data)