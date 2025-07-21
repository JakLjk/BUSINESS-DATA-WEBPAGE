from django.shortcuts import render
from django.http import HttpResponse

from .models import CompanyInfo

# Create your views here.
def index(request):
    companies = CompanyInfo.objects.all().using("data")
    context = {
        'companies':companies
    }
    return render(request, "business_details/index.html", context)

def details(request):
    # Loads from DB
    # Checks if there are records
    # If not then sends request to KRS API to download and loads back from DB
    # If old record then sends request to KRS API to downlaod records
    
    return HttpResponse("details")

def documents(request):
    return HttpResponse("documents")
