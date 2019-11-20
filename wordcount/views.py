from django.http import HttpResponse
from django.shortcuts import render
import operator
import string


def home(request):
    contextA = {"hey": "Now is the time for all good folks."}
    return render(request, 'wordcount/home.html', contextA)


def about(request):
    return render(request, 'wordcount/about.html')


def count(request):
    #
    # remove punctuation
    # map punctuation to space
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    entered_text = str(request.POST.get("entered_text"))
    entered_text = entered_text.translate(translator)
    entered_text = entered_text.lower()
    words = entered_text.split()
    
    character_dictionary={}
    for c in entered_text:
        if c == ' ':

            continue #ignore spaces
        if c in character_dictionary:
            # Increase
            character_dictionary[c] += 1

        else:
            # add to the word_dictionaryword_dictionary[word]=1
            character_dictionary[c] = 1

    sorted_chars = sorted(character_dictionary.items(), key=operator.itemgetter(0))
    sorted_chars = sorted(sorted_chars, key=operator.itemgetter(1), reverse=True)

    word_dictionary={}

    for word in words:
    

        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the word_dictionaryword_dictionary[word]=1
            word_dictionary[word] = 1
        # i+=1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(0))
    sorted_words = sorted(sorted_words, key=operator.itemgetter(1), reverse=True)

    return render(request, 'wordcount/results.html', 
                        {'entered_text': entered_text,
                        'total_chars':len(entered_text),'unique_char_count':len(character_dictionary),
                        
                        'sorted_chars':sorted_chars,
                         'total_words': len(words), 'unique_word_count': len(sorted_words),
                                          'sorted_words': sorted_words})
