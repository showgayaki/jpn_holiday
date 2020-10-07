from django.db import models


class JpnHoliday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name
