from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<!DOCTYPE html>
<html>
<head>
    <title>Index Page</title>
</head>
<body>
    <h1>Index Page</h1>
    <ul>
        <li><a href="http://127.0.0.1:8000/geeks/">GeeksforGeeks</a></li>
        <li><a href="http://127.0.0.1:8000/harry_notes/">Code with Harry Notes</a></li>
        <li><a href="http://127.0.0.1:8000/youtube_lecture/">YouTube Lecture</a></li>
        <li><a href="http://127.0.0.1:8000/django_docs/">Django Documentation</a></li>
    </ul>
</body>
</html>
''')

def geeks(request):
    text=request.GET.get('text')
    print("text",text)
    return HttpResponse('''<h1>Welcome</h1> link : <a href="https://www.geeksforgeeks.org/django-introduction-and-installation/"> click here for geeks for geeks notes</a> {{ text }}''')

def harry_notes(request):
    return HttpResponse('''<h1>Home</h1> link : <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-5/" >click to reach code with harry notes</a>''')

def youtube_lecture(request):
    return HttpResponse('''<h1>YouTube Lecture link:</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7" > click here to watch the video now </a>''')

def django_docs(request):
    return HttpResponse('''<h1>Django Documentation link:</h1> <a href="https://docs.djangoproject.com/en/4.2/intro/tutorial01/">click here to access the documentation</a>''')

def working(request):
    return render(request,"index.html")