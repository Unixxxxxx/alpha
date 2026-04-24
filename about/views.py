from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def Home(request):
    return render (request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(requiest.POST)
        if form.is_valid():
            form.save()
            return render('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def success_view(request):
    return render(request, 'success.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
