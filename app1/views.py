from django.shortcuts import render,redirect
from .forms import loginForm
# Create your views here.
from .models import studentData,Deportment,Pedagogy
def home (request ):
    form = loginForm()
    return render(request,"home.html",{"form":form})

def marklist (request ):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            # print(forms)
            stuId  = form.cleaned_data['studentId']
            dob  = form.cleaned_data['dob']
            print(stuId,dob)
            dat =  list(studentData.objects.filter(dob=dob, applicationNo=stuId).values())
            print(dat)
            if not dat:
                return redirect("home")
            print(dat[0]['deportment_id'])
            deportment = list(Deportment.objects.filter(id=dat[0]['deportment_id']).values("name"))
            print(deportment[0]['name'])
            pedagogy = list(Pedagogy.objects.filter(id=dat[0]['pedagogy_id']).values("subject"))
            print(pedagogy[0]['subject'])
            return render(request,"marklist.html",{"data":dat[0],"deportment":deportment[0]['name'],"pedagogy":pedagogy[0]['subject']})
        return redirect("home")
    return redirect("home") 