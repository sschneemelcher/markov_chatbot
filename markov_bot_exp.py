import pickle
import random

f = open("markov_dict_exp.pkl", "rb")
dict = pickle.load(f)
f.close()
answer = ''

def generate_text(inp, answer):
    inp = inp.lower()
    inpwords = inp.split(' ')
    if len(inpwords) > 2:
        i = 0
        while((str(inpwords[-3]) + ' ' + str(inpwords[-2]) + ' ' + str(inpwords[-1])) in dict.keys()):
            inp = dict[(str(inpwords[-3]) + ' ' + str(inpwords[-2]) + ' ' + str(inpwords[-1]))]
            #print(str(random.choice(inp)))
            inpwords = (str(inpwords[-2]) + ' ' + str(random.choice(inp))).split(' ')
            answer = answer + str(inpwords[-1]) + ' '
            i = i + 1
            #print(answer)
            if i > 80:
                break
        #print('test ' + str(inpwords[-2]) + ' ' + str(inpwords[-1]))
        #answer = answer + str(inpwords[-1])
        generate_text((str(inpwords[-2]) + ' ' + str(inpwords[-1])), answer)
    elif len(inpwords) > 1:
        i = 0
        while((str(inpwords[-2]) + ' ' + str(inpwords[-1])) in dict.keys()):
            inp = dict[(str(inpwords[-2]) + ' ' + str(inpwords[-1]))]
            inpwords = random.choice(inp).split(' ')
            answer = answer + str(inpwords[1]) + ' '
            i = i + 1
            #print(answer)
            if i > 80:
                break

        generate_text(str(inpwords[-1]), answer)
    elif len(inpwords) > 0:
         i = 0
         inpwords = random.choice(list(dict)).split(' ')
         while((str(inpwords[-2]) + ' ' + str(inpwords[-1])) in dict.keys()):
             inp = dict[(str(inpwords[-2]) + ' ' + str(inpwords[-1]))]
             inpwords = random.choice(inp).split(' ')
             answer = answer + str(inpwords[1]) + ' '
             i = i + 1
             if i > 50:
                 break
    else:
        answer = 'please type something. :)'




    return answer

while(1):
    inp = input('You: ')
    answer = generate_text(inp, '')
    if answer == '':
        print('Bot: ' + 'sorry i could not understand you. :)')
    else:
        print('Bot: ' + answer)
        answer = ''
