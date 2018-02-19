import os
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from .utils import get_unique_slug

# Create your models here.


def get_image_path(instance, filename):
    upload_file_name, file_extension = os.path.splitext(filename)
    return '/'.join(['thumbnail_images', instance.slug, instance.title + file_extension])


class PostAndComment(models.Model):
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        abstract=True


class Post(PostAndComment):
    '''blog post'''
    POST_TYPE = (
        ('Data', 'Data'),
        ('PyJava', 'PyJava'),
        ('iOS/Misc', 'iOS/Misc'),
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='post',
        on_delete=models.CASCADE,
        )
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=250, blank=True)
    post_type = models.CharField(
        max_length=15,
        choices=POST_TYPE,
        default=POST_TYPE[0][0],
    )
    thumbnail = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.title in ("new", "data", "pyjava", "ios", "drafts"):
            self.title = self.title + "-post"
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return self.title


class Comment(PostAndComment):
    '''Anon comments'''
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
        )
    author = models.CharField(max_length=250)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()
    
    def __str__(self):
        return self.content[:20]