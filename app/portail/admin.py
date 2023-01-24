from django.contrib import admin
from portail import models as p_models

# Register your models here.

class ParamAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in p_models.Params._meta.get_fields()]
    search_fields = ['name',]


 
# registre
admin.site.register(p_models.Params, ParamAdmin)