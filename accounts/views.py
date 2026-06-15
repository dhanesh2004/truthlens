from django.shortcuts import render, redirect
from .forms import SignUpForm

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            print("FORM IS VALID")
            form.save()
            print("USER SAVED")
            return redirect('home')

        else:
            print(form.errors)

    else:
        form = SignUpForm()

    return render(
        request,
        'accounts/signup.html',
        {'form': form}
    )