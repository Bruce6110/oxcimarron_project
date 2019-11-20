from django.shortcuts import render


quotes = (
    "A wise man is superior to any insults which can be put upon him, and the best reply to unseemly behavior is patience and moderation.  -- Molière",
    "Oh, how fine it is to know a thing or two.  -- Molière",
    "The greater the obstacle, the more glory in overcoming it.  -- Molière",
    "People don't mind being mean; but they never want to be ridiculous  -- Molière",
    "Tell me, what is it you plan to do with your one wild and precious life?  -- Mary Oliver",
    "When anger rises, think of the consequences.  -- Confucius",
    "Our greatest glory is not in never falling, but in rising every time we fall.  -- Confucius",
    "The art of being wise is the art of knowing what to overlook.  -- William James",





)  # note that we use a tuple, not a list, because the context needs unmutable keys


def home(request):

    return render(request, 'home.html', {"quotes": quotes})


def orientation(request):
    return render(request, 'orientation.html')
