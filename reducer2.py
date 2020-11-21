##### reducer2.py beinhaltet die Dokumentenfrequenz und liefert ein absteigend sortiertes und normalisiertes Ergebnis ################
import sys
import operator
import os

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
    wordcount = {}
    for line in sys.stdin:
        word, n = line.strip().split('\t', 1)
        n = int(n)
        if word in wordcount:
            wordcount[word] += n 
        else:
            wordcount[word] = n
    
    sorted_dict = sorted(wordcount.items(), key=operator.itemgetter(1))
    sorted_dict.reverse()

    doccount = {}
    for i in os.listdir('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_library'):
        with open("/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_library/"+i,"r") as file:
            doc_file=file.read()
            doc_file = doc_file.lower()
            doc_file = clean(doc_file)
            for i in range(len(sorted_dict)):
                if sorted_dict[i][0] in doc_file:
                    if sorted_dict[i][0] in doccount:
                        doccount[sorted_dict[i][0]] += 1
                    else:
                        doccount[sorted_dict[i][0]] = 1
    
    normcount = {}
    for key in wordcount:
        normcount.update({key:wordcount[key]/doccount[key]})

    sorted_dict_norm = sorted(normcount.items(), key=operator.itemgetter(1))
    sorted_dict_norm.reverse()


    for key in sorted_dict_norm:
        print('%s\t%s' %(key[1],key[0]))


if __name__ == "__main__":
    main()



