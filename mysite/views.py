#I have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    checkStatus=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get("newlineremove",'off')
    extraspaceremover=request.POST.get("extraspaceremover",'off')
    charcounter=request.POST.get("charcounter",'off')
    punctuations='''!()-[]{};:'"\,<>./>?@#$%^&*_~'''
    purpose=""
    analyzed = ""
    if checkStatus=="on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed
        purpose=purpose+'Removed Punctuation'
    if fullcaps=='on':
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext = analyzed
        purpose=purpose+'Changed To Uppercase'
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char
        djtext=analyzed
        purpose=purpose+'Removed new lines'
    if extraspaceremover=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext=analyzed
        purpose = purpose+'Removed extra space'
    if charcounter=="on":
        counter=0
        for i in djtext:
            counter=counter+1
        analyzed="this string contains "+ str(counter) + " characters"
        analyzed=djtext+analyzed
        purpose=purpose+'Count'
        djtext=analyzed
    param = {'purpose': 'Count', 'analyzed_text': djtext}
    if not (charcounter=="on" or extraspaceremover=="on" or newlineremover=="on" or fullcaps=='on' or checkStatus=="on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', param)
