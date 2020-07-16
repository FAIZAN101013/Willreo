from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import upload
from .forms import uploadForm

# Create your views here.

def upload_page(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')  
    else:
        form = uploadForm()

    return render(request, 'upload.html', {'form': form})



def main(request):
    
    loads = upload.objects.all()

    return render(request, 'main_page.html', {'loads': loads})


def main_stu(request):
    
    loads = upload.objects.all()

    return render(request, 'main_page_stu.html',{'loads': loads})



def profile(request):
    return render(request, 'profile.html')

def help(request):
    return render(request, 'help.html')

def profile_stu(request):
    return render(request, 'profile_stu.html')

def help_stu(request):
    return render(request, 'help_stu.html')
