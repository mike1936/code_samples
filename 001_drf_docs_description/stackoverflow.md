# Summary

There are three type of descriptions in DRF docs (as I have tried), they relies on set-ups in two locations.

- **Type 1**: Path Parameter Description -> set at model field definition
- **Type 2**: Query Parameter Description -> set at filter definition for specific field
- **Type 3**: Request Body Description -> same as Type 1

## Model field definition for Type 1 & Type 3 descriptions

    # my_project/my_app/models.py
    from django.db import models
    from django.utils.translation import gettext_lazy as _

    class MyModel(models.Model):
        id = models.BigAutoField(primary_key=True, help_text=_("Field id - This will show up in DRF docs Path Parameter Description/Request Body Description, '_' meaning using django translation module"))
        field1 = models.IntegerField(help_text=_("Field field1 - This will show up in DRF docs Path Parameter Description/Request Body Description, '_' meaning using django translation module"))

## SearchFilter for specific field definition for Type 2 description

    # my_project/my_app/filters.py
    from rest_framework import filters

    class MyFilter(filters.SearchFilter):
        search_param = 'field1'
        search_title = 'Exact matches Field1' # Shows up in DRF docs interactive query pop-up menu as the title for the query section of the field1
        search_description = 'This will show up in DRF docs Query Parameter Description'

## Serializer and ViewSet configs

    # my_project/my_app/serializers.py
    from rest_framework import serializers

    from my_app.models import MyModel

    class MySerializer(serializers.ModelSerializer):
        class Meta:
            model = MyModel
            fields = '__all__'

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

## Finally the urls and settings configuration

    # my_project/my_app/urls.py
    from django.urls import path, include
    from rest_framework import routers

    from my_app.views import MyViewSets

    router = routers.DefaultRouter()
    router.register('test', MyViewSets)

    urlpatterns = [
        path('', include(router.urls))
    ]

    # my_project/my_project/urls.py
    from django.urls import path, include
    from rest_framework.documentation import include_docs_urls

    urlpatterns = [
        path('docs/', include_docs_urls('API Documentaion')),
        path('my_app/', include('my_app.urls'))
    ]

Demo here: [drf_docs_description](https://github.com/mike1936/code_samples/tree/main/001_drf_docs_description/my_project)
