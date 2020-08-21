from django.shortcuts import render,redirect
from users.forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        reg_form=UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,f'Account created, Please login now!')
            return redirect("login")
    else:
        reg_form=UserRegisterForm()
    return render(request,"users/register.html",{'reg_form':reg_form})
