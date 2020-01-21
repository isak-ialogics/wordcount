from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split(' ')
    worddict = {}
    for word in wordlist:
        if word in worddict:
            #Increase word count
            worddict[word] += 1
        else:
            #Add to worddict
            worddict[word] = 1

    count = len(wordlist)
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': count, 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')
