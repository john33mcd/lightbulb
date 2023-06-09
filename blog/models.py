from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


choices = [
    ('awful', 'awful'),
    ('bad', 'bad'),
    ('ok', 'ok'),
    ('good', 'good'),
    ('excellent', 'excellent'),
]


class Review(models.Model):
    title = models.CharField(
        max_length=200, unique=True, default="Please give your review a title")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_list")
    review_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=20, choices=choices, default='ok')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.author}: {self.rating}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Review, self).save(*args, **kwargs)
