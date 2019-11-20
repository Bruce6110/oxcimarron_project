from django.shortcuts import render

# Create your views here.

def compass(request):
    return render(request, 'sensors/compass.html')

def gravity(request):
    return render(request, 'sensors/gravity.html')    

def cooking(request):
    return render(request, 'sensors/cooking.html')        

def speech_recognition(request):
    return render(request, 'sensors/speech_recognition.html')    

def speech_synthesis(request):
    return render(request, 'sensors/speech_synthesis.html')    