from django.shortcuts import render
from .forms import UserRegisterForms

# Create your views here.
# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForms(request.POST)
#         if form.is_valid():
#             form.save()
#             username