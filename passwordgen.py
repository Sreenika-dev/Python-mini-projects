import random

#generating random values from 65 to 90 and converting ascii codes to characters
capitalCase1 = chr(random.randint(65,90))
capitalCase2 = chr(random.randint(65,90))
smallCase1 =  chr(random.randint(97,122))
smallCase2 =  chr(random.randint(97,122))
digit1 = random.randint(0,9)
digit2 = random.randint(0,9)
punctMarks1 =  chr(random.randint(33,152))
punctMarks2 = chr(random.randint(33,152))


#concatenating every character and turning them into string
password = capitalCase1+smallCase1+capitalCase2+smallCase2+str(digit1)+str(digit2)+punctMarks1+punctMarks2


#function to shuffle the string(by converting string into list)
def shuffle(s):
    list1 = list(s)
    random.shuffle(list1)
    return ''.join(list1)
shuffle(password)
print(password)   

