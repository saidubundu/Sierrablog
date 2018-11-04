from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Post(models.Model):
    author = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=150)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title

            def get_absolute_url(self):
                return reverse('blog.views.post', args=[self.slug])
