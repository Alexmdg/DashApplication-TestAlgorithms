from django.shortcuts import render


def lists(request):
    return render(request, 'Lists/index.html')