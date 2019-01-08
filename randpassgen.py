# Ahad H. Shabbir
# r/dailyprogrammer Challange #3
# Random Password Generator

import random, re, string

def getPasswds(
        num: int, 
        length: int, 
        needUpperCase=True, 
        needLowerCase=True,
        needDigit=True, 
        needPunc=True
        ) -> [str]:

    # Ternery operator wrapper for convience:
    getIf = lambda string, truth: string if truth else ''
    
    # Check if all specifications are false:
    if not (needUpperCase or needLowerCase or needDigit or needPunc):
        raise Exception('At least one specification must be true.')
    
    # Build a list of charecters to choose from:
    charList = ''
    charList += getIf(string.ascii_lowercase, needLowerCase)
    charList += getIf(string.ascii_uppercase, needUpperCase)
    charList += getIf(string.digits, needDigit)
    charList += getIf(string.punctuation, needPunc)
    print(charList)

    # Build regex object:
    regexStr = '['
    regexStr += getIf('A-Z', needUpperCase)
    regexStr += getIf('a-z', needLowerCase)
    regexStr += getIf('0-9', needDigit)
    regexStr += getIf(string.punctuation, needPunc)
    regexStr += ']+'
    regexStr = '' if regexStr == '[]+' else regexStr
    print(regexStr)
    passwd_check_re = re.compile(regexStr)

    # Get 'num' number of randomized passwords with length 'length':
    passwds = []
    
    while len(passwds) != num:
        passwd = ''
        for _ in range(length):
            index = random.randint(0, len(charList) - 1)
            passwd += charList[index]
        if passwd_check_re.fullmatch(passwd):
            print(passwd)
            passwds.append(passwd)
    
    return passwds

print(getPasswds(3, 16))