from django.http import HttpResponse
from django.shortcuts import render

def gopi(request):
    return HttpResponse("Hai Gopi")

def home1f(request):
    return HttpResponse("<h1>Welcome!!</h1>")

def homef(request):
    return render(request, "home.html")

def registerf(request):
    return render(request, "myweb.html")

def mywordsf(request):  # This is the funtion to when user types 'mymessage' in url of webpage
    return render(request, "mywords.html")

def countf(request):   # This is the funtion to when user click the 'Count Words' button in mywords.html
    mywords=request.GET['mymessage']  #here 'mymessage' name value we given in 'textarea' tag in mywords.html
    splitwords = mywords.split()
    return render(request, "countwords.html", {"message": mywords, "wordscount": len(splitwords)}) #we are passing "message" and "wordscount" values to the countwords.html