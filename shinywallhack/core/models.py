
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


@python_2_unicode_compatible
class Domain(models.Model):
    domain = models.CharField(max_length=128)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.domain
