from django.shortcuts import render

# Create your views here.
def Home(request):
    return render (request, 'index.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
