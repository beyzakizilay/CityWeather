# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import login
# from .forms import RegisterForm

# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data["username"],
#                 email=form.cleaned_data["email"],
#                 password=form.cleaned_data["password"]
#             )
#             login(request, user)
#             return redirect("index")
#     else:
#         form = RegisterForm()
#     return render(request, "accounts/register.html", {"form": form})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})
