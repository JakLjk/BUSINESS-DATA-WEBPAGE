from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import CompanyInfo, KrsDfDocuments

# Create your views here.
def index(request):
    return render(request, "business_details/index.html")

def search_results(request):
    context = {}
    search_entry = request.GET.get("search_entry")
    try:
        context["companies"] = CompanyInfo.objects.using("data").filter(
            Q(krs_number__icontains=search_entry)
            |
            Q(full_name__icontains=search_entry)
            |
            Q(nip_number__icontains=search_entry)
            |
            Q(regon_number__icontains=search_entry)
            ,
            is_current=True

        )

        return render(request, "business_details/search.html", context)
    except:
        return HttpResponse(f"Not found - {search_entry}")



def details(request, company_id):
    context = {}
    company = get_object_or_404(CompanyInfo.objects.using("data"), pk=company_id)
    context["company"] = company 
    financial_documents_count = (KrsDfDocuments
                           .objects
                           .using("data")
                           .filter(krs_number=company.krs_number)
                           .count())
    context["financial_documents_count"] = financial_documents_count

    return render(request, "business_details/details.html", context)

def documents(request, company_id):
    context = {}
    company = get_object_or_404(CompanyInfo.objects.using("data"), pk=company_id)
    context["company"] = company
    documents = (KrsDfDocuments
                           .objects
                           .using("data")
                           .filter(krs_number=company.krs_number)
                           .values(
                               "hash_id", 
                               "document_type", 
                               "document_date_from",
                               "document_date_to"))
    context["documents"] = documents
    return render(request, "business_details/documents.html", context)
