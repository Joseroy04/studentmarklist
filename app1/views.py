from django.shortcuts import render,redirect
from .forms import loginForm
# Create your views here.

def home (request ):
    form = loginForm()
    return render(request,"home.html",{"form":form})

def marklist (request ):
    if request.method == "POST":
        forms = loginForm(request.POST)
        if forms.is_valid:
            print(forms)
            stuId  = forms.cleaned_data['studentId']
            dob  = forms.cleaned_data['dob']
            
            return render(request,"marklist.html",{"id":stuId,"dob":dob})
        return render(request,"marklist.html",{})
    return redirect("home") 