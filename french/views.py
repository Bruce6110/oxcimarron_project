import os
from django.shortcuts import render
from django.core.files import File
# Create your views here.


class Exercise():

    TITLES={'A':'Marie et le dentiste','B':'Julie de Jamaïque','C':'Marie s\'est ennuie',
            'D':'Si j\'étais un athlète','E':'Le restaurant brûlé','F':'J\'aime que les choses soient bien organisées','G':'Mon expérience universitaire jusqu\'à présent','H':'Notre journée au musée','I':'Ma grand-mère extraordinaire'}
    LETTERS=['A','B','C','D','E','F','G','H','I']

    def __init__(self,letter,parts):
        self.letter=letter
        
        self.parts=parts
        
    def title(self):
        return Exercise.TITLES[self.letter]

    def __str__(self):
        print(self.parts)
        return "%s %s" % (self.letter, self.title)

    class Meta:
        ordering = ['letter']


def exercises(request):
    print('here')
    exercises=[]
    debugInfo=""
    for letter in Exercise.LETTERS:
        
        parts=[]
        try:
            for number in range(0,3):
                file = open('static/exercise'+str(letter)+'-'+str(number)+'.txt','r',encoding='utf-8')
                parts.append(file.read())
        
            x=Exercise(letter,parts)
           
            exercises.append(x)
        except Exception as e:
            print(e.__str__)
            debugInfo+=str(type(e))+" --- "+str(e.args)
            


    
    return render(request, 'french/exercises.html', {'page_title': 'French Grammar Exercises','exercises':exercises,'debugInfo':debugInfo})


def home(request):
    return render(request, 'french/home.html')
