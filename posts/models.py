from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

def get_default_category():
    categories = [
        {'name': 'Uncategorized', 'slug': 'uncategorized'},
        {'name': 'Fun', 'slug': 'fun'},
        {'name': 'Inspirational', 'slug': 'inspirational'},
        {'name': 'Adventure', 'slug': 'adventure'},
    ]

    for category in categories:
        Category.objects.get_or_create(name=category['name'], slug=category['slug'])

    default_category, created = Category.objects.get_or_create(name='Uncategorized', slug='uncategorized')
    return default_category.id

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=get_default_category)
    
    image = models.ImageField(
        upload_to='images/', default='../default_post_tjnjpe', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'