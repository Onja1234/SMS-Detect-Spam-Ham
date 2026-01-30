from django.shortcuts import render

def home(request):
    return render(request, 'spam_detection/index.html')
