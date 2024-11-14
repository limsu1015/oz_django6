from django.db import models


class BaseModel(models.Model):
    up_dated = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class User(models.Model):
    name = models.CharField(max_length=50)
    up_dated = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    up_dated = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    up_dated = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
