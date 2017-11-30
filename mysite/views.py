from django.shortcuts import render, get_object_or_404
from mysite.models import Pizza


def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'a1': pizzas})


# return render(request, 'index.html')
# return render(request, 'index.html', {'insert_me': "Я из views.py"})


def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'pizza_detail.html', {'apizza': pizza})
