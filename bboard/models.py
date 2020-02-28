from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Ads'
        verbose_name = 'Ad'
        ordering = ['-published']


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']