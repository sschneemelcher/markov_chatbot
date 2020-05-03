import pickle
import random

f = open("markov_dict.pkl", "rb")
dict = pickle.load(f)
f.close()


def generate_text(inp):
    inp = inp.lower()
    answer = ''
    inpwords = inp.split(' ')
    if len(inpwords) > 1:
        i = 0
        while((str(inpwords[-2]) + ' ' + str(inpwords[-1])) in dict.keys()):
            inp = dict[(str(inpwords[-2]) + ' ' + str(inpwords[-1]))]
            inpwords = random.choice(inp).split(' ')
            answer = answer + str(inpwords[1]) + ' '
            i = i + 1
            #print(answer)
            if i > 80:
                break
    else:
         i = 0
         inpwords = random.choice(list(dict)).split(' ')
         while((str(inpwords[-2]) + ' ' + str(inpwords[-1])) in dict.keys()):
             inp = dict[(str(inpwords[-2]) + ' ' + str(inpwords[-1]))]
             inpwords = random.choice(inp).split(' ')
             answer = answer + str(inpwords[1]) + ' '
             i = i + 1
             if i > 50:
                 break
            #print(answer)


    return answer

while(1):
    inp = input('')
    print(generate_text(inp))
