path = '../training_data.txt'

dict = {}

with open(path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

for line in lines:
    line.replace('\t', ' ')
    words = line.split(' ')
    for i in range(len(words) - 2):
        if((str(words[i]) + ' ' + str(words[i+1])) in dict.keys()):
            dict[str(words[i]) + ' ' + str(words[i+1])].append(str(words[i+1]) + ' ' + str(words[i+2]))
        else:
            dict[str(words[i]) + ' ' + str(words[i+1])] = [(str(words[i+1]) + ' ' + str(words[i+2]))]


print(dict)
