from django.shortcuts import render

# Create your views here.

def home(request):return render(request, 'itreporting/home.html', {'title': 'Welcome Page'})
def about(request):return render(request, 'itreporting/about.html')
def contact(request):return render(request, 'itreporting/contact.html')