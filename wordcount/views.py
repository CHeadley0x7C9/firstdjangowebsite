

from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')


def aboutpage(request):
	return render(request,'about.html')


def contactpage(request):
	return HttpResponse('<h1>CONTACT</h1>')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()

	wordDict = {}

	for word in wordlist:
		if word in wordDict:
			wordDict[word.lower()] +=1
		else:
			wordDict[word.lower()] = 1

	sortedwords = sorted(wordDict.items(), key=operator.itemgetter(1),reverse= True)


	return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist), 'sortedwords':sortedwords})