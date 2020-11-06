# my_project/my_app/views.py
from rest_framework import viewsets

from my_app.models import MyModel
from my_app.serializers import MySerializer
from my_app.filters import MyFilter

class MyViewSets(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    filter_backends = [MyFilter]
    search_fields = ['=field1', '@field1']
        # The first charactor '='/'^' is used by SearchFilter.filter_queryset while doing
        # the SearchFilter.construct_search method
        # and '=' for exact match while '^' for starts with search
        # One could get all options at rest_framework.filters.SearchFilter.lookup_prefixes
        # BTW my rest_framework version is djangorestframework==3.11.1
