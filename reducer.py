import sys
def main():
    count = {}
    for line in sys.stdin:
        word, n = line.strip().split('\t', 1)
        n = int(n)
        if word == '-':
            count[word] = 0
        elif word in count:
            count[word] += n 
        else:
            count[word] = n
    for key in count:
        if count[key] >= 1:
            print('%s\t%s' %(key,count[key]))

if __name__ == "__main__":
    main()



