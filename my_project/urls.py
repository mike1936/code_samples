# my_project/my_project/urls.py
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls('API Documentaion')),
    path('my_app/', include('my_app.urls'))
]
