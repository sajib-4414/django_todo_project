from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

#Category
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)