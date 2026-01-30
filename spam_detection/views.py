from django.shortcuts import render
from .services import predict_spam

def home(request):
    return render(request, "spam_detection/index.html")

def detect(request):
    result = None
    message = ""

    if request.method == "POST":
        message = request.POST.get("message")
        result = predict_spam(message)

    return render(request, "spam_detection/result.html", {
        "result": result,
        "message": message
    })
