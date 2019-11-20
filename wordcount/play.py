
import os

#print a dictionary
def printDictionary(dict={}):

    dict=os.environ
    #dict={"a":1,"b":2,"c":3}
    print(dict)
    for key, value in dict.items():
        print(key+":    "+str(value))


printDictionary(os.environ)

#Rename a file
# os.rename("t.txt","u.txt")
