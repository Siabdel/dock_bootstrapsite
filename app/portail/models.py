from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Params(models.Model):
    class ThemesModel(models.TextChoices):
        AGENCY = 'AG', _('Agency')
        MATERIAL = 'MT', _('Material')

    name    = models.CharField(max_length=100)
    c_value = models.CharField(max_length=100, 
                               choices=ThemesModel.choices,
                               default=ThemesModel.AGENCY)
    description = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()