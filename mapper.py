import sys
import re
def clean_word(word):
    return re.sub(r'[^\w\s\-]','',word).lower()
    #return re.sub(r'[^A-Za-z0-9]+', '', word).lower()

def main():
    for line in sys.stdin:
        wordlist = line.strip().split()
        for word in wordlist:
            print('%s\t%s' % (clean_word(word), 1))

if __name__ == "__main__":
    main()