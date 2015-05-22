from django.db import models

# Create your models here.


class CWE(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)

    def __unicode__(self):
        return "CWE-%s - %s" % (self.code, self.name)

