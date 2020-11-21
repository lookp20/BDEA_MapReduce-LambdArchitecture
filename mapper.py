######## python __version__ 2.6.6 ##############
import sys
import re

def clean(word):
    word = word.replace('\xc3\x84', 'ae')
    word = word.replace('\xc3\x96', 'oe')
    word = word.replace('\xc3\x9c', 'ue')
    word = word.replace('\xc3\x9f', 'ss')
    word = word.replace('\xc3\xa4', 'ae')
    word = word.replace('\xc3\xb6', 'oe')
    word = word.replace('\xc3\xbc', 'ue')
    word = word.replace('\xc5\xbf', 's')
    word = word.replace('u\xcd\xa4', 'ue')
    word = word.replace('a\xcd\xa4', 'ae')
    word = word.replace('o\xcd\xa4', 'oe')
    word = word.replace('\xc5\xbf', 's')
    word = word.replace('U\xcd\xa4', 'ue')
    word = word.replace('A\xcd\xa4', 'ae')
    word = word.replace('O\xcd\xa4', 'oe')    
    return word

def main():
   
    for line in sys.stdin:
        line = clean(line)
        wordlist = re.findall(r"[\w']+", line)
        for word in wordlist:
            print('%s\t%s' % (word.lower(), 1))

if __name__ == "__main__":
    main()
