from django.db import models
from django_summernote.fields import SummernoteTextField
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created_on')
    content = models.TextField()
    short_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    cover_image = models.ImageField(upload_to='images/', null=True, blank=True)
    class Meta:
        ordering = ('-created_on',)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
