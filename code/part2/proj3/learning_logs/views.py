from django.shortcuts import render

# Create your views here.

def index(request):
    """Mainpage of Learning_logs"""

    return render(request,'learning_logs/index.html')
