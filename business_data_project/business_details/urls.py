from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:company_id>/", views.details, name="details"),
    path("<int:company_id>/documents", views.documents, name="documents"),
]
