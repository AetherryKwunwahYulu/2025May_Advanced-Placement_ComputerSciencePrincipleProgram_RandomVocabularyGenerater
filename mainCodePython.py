def RandWord(lst2d):
    randNum = random.randint(0,len(lst2d)-1)
    ans = input(lst2d[randNum][1])
    if ans == lst2d[randNum][0]:
        return True
    else:
        return False
    
def WordExel(lst):
    uWordLst = []
    for i in range(0,len(lst)-1) :
        tempLst = (lst[i].split(sep=','))
        if len(tempLst) == 2: 
            uWordLst.append([tempLst[0], tempLst[1]])
        else:
            print('Illegal input')
    return uWordLst    

def CheckWord():
    newOne = ' '
    while(not newOne == 'No'):
        ansB = RandWord(WordExel(oriWordLst))
        if ansB == True:
            print('You are Right!')
            newOne = input("One more? Type in 'Yes' else 'No'.")
        else:
            print('False')
            newOne = input("One more? Type in 'Yes' else 'No'.")

    
import random
print('Pls type in your words and the marked words in form of "theword,thekey".\n Input "0,0" if your finished your word lists.')
oriWordLst = []
tempInWord = ' '
while (not(tempInWord =='0,0')):
    tempInWord = input()
    oriWordLst.append(tempInWord)
    print('Your word is stored. Tap enter to input a new word.')
if len(oriWordLst)==0 :
    print('No word was typed in Or Illegal input.')
else:
    CheckWord()
