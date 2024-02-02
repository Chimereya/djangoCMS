from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = TaggableManager()
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/images', blank=True, null=True)
    image_credit = models.URLField(null=True, help_text="paste or type the link(optional)", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.slug])

    class Meta:
        ordering = ['date_created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def num_of_likes(self):
        return self.likes.count()