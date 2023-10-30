from django.shortcuts import render


def homepage(request):
    context = {"product": "product"}
    return render(request, 'Home_Page.html', context)