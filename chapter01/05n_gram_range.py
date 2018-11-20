target = "I am an NLPer"
words = target.split(" ")
result = [];
num = 0;
for val in range(len(words)-1):
    result.append(words[num:num+2])
    num += 1
print(result);
string_result = []
num = 0
for val in range(len(target)-1):
    string_result.append(target[num:num+2]) 
    num += 1
print(string_result)


