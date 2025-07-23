from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="company-index"),
    path("search", views.search_results, name="company-search"),
    path("<int:company_id>/details", views.details, name="company-details"),
    path("<int:company_id>/documents", views.documents, name="company-documents"),
]
