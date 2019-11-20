import re
import operator
import string

with open('ulysses.txt', 'r') as f:
 #   count=0
 #   for line in f:

 #      for word in line.split():
 #           count=count+1
 #          if count%10000==0:
 #              print(count)

 #   print("Total words: "+str(count))
    count = 0
    words = []
    word_dictionary = {}
    linecount=0
    wordcount=0    
    for line in f:
        linecount+=1
        words = re.findall(r"[\w]+|[^\s\w]", line)
        wordcount+=len(words)

        for word in words:
            word=word.lower()
            if word in word_dictionary:
                # Increase
                word_dictionary[word] += 1
            else:
            # add to the word_dictionaryword_dictionary[word]=1
        
                word_dictionary[word] = 1
            
        # i+=1
    print("Word dictionary is "+str(len(word_dictionary))+"words long")
    print("Total words = "+str(wordcount))

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(0))
    sorted_words = sorted(
        sorted_words, key=operator.itemgetter(1), reverse=True)
    with open("Output.txt", "w") as text_file:

        for word, counttotal in sorted_words:
            print(word+" - "+str(counttotal), file=text_file)
