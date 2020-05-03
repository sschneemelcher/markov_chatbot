import pickle

path = '../training_data.txt'

dict = {}

with open(path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

for line in lines:
    line = line.lower()
    line = line.replace('\t', ' ')
    words = line.split(' ')
    for i in range(len(words) - 2):
        if((str(words[i]) + ' ' + str(words[i+1])) in dict.keys()):
            dict[str(words[i]) + ' ' + str(words[i+1])].append(str(words[i+1]) + ' ' + str(words[i+2]))
        else:
            dict[str(words[i]) + ' ' + str(words[i+1])] = [(str(words[i+1]) + ' ' + str(words[i+2]))]
    for i in range(len(words) - 3):
        if((str(words[i]) + ' ' + str(words[i+1]) + ' ' + str(words[i+2])) in dict.keys()):
            dict[str(words[i]) + ' ' + str(words[i+1]) + ' ' + str(words[i+2])].append(str(words[i+2]) + ' ' + str(words[i+3]))
        else:
            dict[str(words[i]) + ' ' + str(words[i+1]) + ' ' + str(words[i+2])] = [(str(words[i+2]) + ' ' + str(words[i+3]))]


print(dict)


f = open("markov_dict_exp.pkl","wb")
pickle.dump(dict,f)
f.close()
