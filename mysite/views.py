from django.shortcuts import render
from mysite.models import Pizza

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'a1': pizzas})

# return render(request, 'index.html')
    # return render(request, 'index.html', {'insert_me': "Я из views.py"})
