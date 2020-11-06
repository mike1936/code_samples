# my_project/my_app/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class MyModel(models.Model):
    id = models.BigAutoField(primary_key=True, help_text=_("Field id - This will show up in DRF docs Path Parameter Description/Request Body Description, '_' meaning using django translation module"))
    field1 = models.IntegerField(help_text=_("Field field1 - This will show up in DRF docs Path Parameter Description/Request Body Description, '_' meaning using django translation module"))
