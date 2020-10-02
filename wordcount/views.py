from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET["fulltext"]
    #print (fulltext)
    worddictionary = {}

    wordlist = fulltext.split()

    for word in wordlist:
        if word not in worddictionary:
            worddictionary[word] = 0
        
        worddictionary[word] += 1

    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "result.html", {"fulltext": fulltext, "length": len(wordlist), "sorted_words": sorted_words})

def about(request):
    return render(request, "about.html")

def test(request):
    return render(request, "home.html", {"key": "value"})

def sh(request):
    return HttpResponse("<h1>Sh</h1>")