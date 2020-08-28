from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')   #this ensures that only logged in user can see the homepage
# Homepage view you can customize it to make it your landing page
def Homepage(request):    
    context = {}
    return render(request, 'Tutorial/index.html',context)

#register form view
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account created for " + user)  #messages are used to display alerts to user, see documentation
            return redirect('login')  #If success redirect to login page for user to login
    context = {'form': form}
    return render(request, 'Tutorial/register.html', context)

#Login view 
# No model required as it is used to just verify user from existing model
def loginpage(request):
    if request.method == 'POST':
        #collect the credentials of user
        usr = request.POST.get('username')
        pas = request.POST.get('password')
        #use authenticate to check for user
        user = authenticate(request, username=usr, password=pas)

        # if success:
        if user is not None:
            login(request, user)
            return redirect('Homepage') #redirect to homepage if valid user
        else:
            messages.info(request, "Username or Password is incorrect") #else show error

    context = {}
    return render(request, 'Tutorial/login.html', context)
#logout view 
#No template as of now, just redirect user to login page
def logoutUser(request):
    logout(request)
    return redirect('login')   