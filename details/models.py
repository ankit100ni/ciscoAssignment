from django.db import models


class RouterProperties(models.Model):
    SAPId = models.CharField(max_length=30)
    HOSTNAME = models.CharField(max_length=20)
    LoopBack = models.CharField(max_length=20)
    MacAddress = models.CharField(max_length=20)

    def __str__(self):
        return self.SAPId

