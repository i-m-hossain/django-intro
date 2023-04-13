from django.shortcuts import render

# Create your views here.


def getUser(request):
    person = {"name": "rafiqul", "age": 23}
    return render(request, 'user/user.html', context=person)
