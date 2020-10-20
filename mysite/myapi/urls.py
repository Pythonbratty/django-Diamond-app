from django.urls import path
from .views import HealthListView

urlpatterns= [

    path("api/health", HealthListView.as_view()),

]