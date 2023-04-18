from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    body = models.CharField(max_length=255, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, verbose_name='Автор')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=255, verbose_name="Комментарий")
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


class Mark(models.Model):
    mark_value = models.CharField(max_length=20, choices=[
        ("Like", "Like"),
        ("Dislike", "Dislike")
    ])
    tweet = models.OneToOneField(Tweet, on_delete=models.CASCADE)

