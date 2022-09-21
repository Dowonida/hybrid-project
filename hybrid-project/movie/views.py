from django.shortcuts import render
from shared.search import search

# Create your views here.

def main(request):


    return render(request, 'movie/main.html')