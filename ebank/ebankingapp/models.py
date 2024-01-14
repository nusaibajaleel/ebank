from django.db import models
from django.urls import reverse
# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='district',blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='district'
        verbose_name_plural='districts'

    def get_url(self):
        return reverse('ebankingapp:branch_by_district',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Branch(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='branch', blank=True)
    branch=models.ForeignKey(District,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def get_url(self):
        return reverse('ebankingapp:branchdetail',args=[self.branch.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Account(models.Model):
    name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.name)

