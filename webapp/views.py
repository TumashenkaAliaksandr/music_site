from django.shortcuts import render

app_name = 'webapp'

def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def blog(request):
    return render(request, 'webapp/blog.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def events(request):
    return render(request, 'webapp/events.html')

def gallery(request):
    return render(request, 'webapp/gallery.html')

def base(request):
    return render(request, 'webapp/base.html')