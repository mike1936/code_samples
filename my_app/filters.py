# my_project/my_app/filters.py
from rest_framework import filters

class MyFilter(filters.SearchFilter):
    search_param = 'field1'
    search_title = 'Exact matches Field1' # Shows up in DRF docs interactive query pop-up menu as the title for the query section of the field1
    search_description = 'This will show up in DRF docs Query Parameter Description'
