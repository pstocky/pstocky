from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True,unique=True)
    name = models.CharField(max_length=10,default=False)
    phone = models.IntegerField()
    idtype = models.CharField(max_length=10,default='IDCard')
    idnum = models.CharField(max_length=20,unique=True)
    isadult = models.BooleanField(default=True)
    isman = models.BooleanField(default=True)
    type = models.CharField(max_length=10,default='VIP')

    class Meta:
        ordering = ('created',)
        db_table = ('VIP')
    def __str__(self):
        return self.name