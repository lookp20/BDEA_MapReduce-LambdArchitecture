######## python __version__ 2.6.6 ##############
import sys
import re

def clean(word):
    if '\xc3\x84' in word:
        return word.replace('\xc3\x84', 'ae')
    elif '\xc3\x96' in word:
        return word.replace('\xc3\x96', 'oe')
    elif '\xc3\x9c' in word:
        return word.replace('\xc3\x9c', 'ue')
    elif '\xc3\x9f' in word:
        return word.replace('\xc3\x9f', 'ss')
    elif '\xc3\xa4' in word:
        return word.replace('\xc3\xa4', 'ae')
    elif '\xc3\xb6' in word:
        return word.replace('\xc3\xb6', 'oe')
    elif '\xc3\xbc' in word:
        return word.replace('\xc3\xbc', 'ue')
    elif '\xc5\xbf' in word:
        return word.replace('\xc5\xbf', 's')
    elif 'u\xcd\xa4' in word:
        return word.replace('u\xcd\xa4', 'ue')
    elif 'a\xcd\xa4' in word:
        return word.replace('a\xcd\xa4', 'ae')
    elif 'o\xcd\xa4' in word:
        return word.replace('o\xcd\xa4', 'oe')
    elif '\xc5\xbf' in word:
        return word.replace('\xc5\xbf', 's')
    elif 'U\xcd\xa4' in word:
        return word.replace('U\xcd\xa4', 'ue')
    elif 'A\xcd\xa4' in word:
        return word.replace('A\xcd\xa4', 'ae')
    elif 'O\xcd\xa4' in word:
        return word.replace('O\xcd\xa4', 'oe')
        
    return word

def main():
   
    for line in sys.stdin:
        line = clean(line)
        wordlist = re.findall(r"[\w']+", line)
        for word in wordlist:
            print('%s\t%s' % (word.lower(), 1))

if __name__ == "__main__":
    main()
