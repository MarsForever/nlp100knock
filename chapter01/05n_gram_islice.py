from itertools import islice
target = "I am an NLPer"
words = target.split(" ")
result = [];
num = 0;
for idx, val in enumerate(islice(words, len(words)-1)):
    result.append(words[idx:idx+2])
print(result);
string_result = []
for idx ,val in enumerate(islice(target, len(target)-1)):
    string_result.append(target[idx:idx+2]) 
print(string_result)


