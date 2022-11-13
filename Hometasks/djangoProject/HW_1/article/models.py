from django.db import models
from django.core.exceptions import ValidationError


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.PROTECT, blank=True, null=True,
        related_name='posts'
    )
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание', null=False, blank=False)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    comment = models.TextField(max_length=500, verbose_name='Комментарий', null=False, blank=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.published} {self.title}'

    def clean(self):
        errors = {}
        if not self.title:
            errors['title'] = ValidationError(
                'Укажите заголовок (название) статьи'
            )
        if not self.content:
            errors['content'] = ValidationError(
                'Заполните содержание статьи'
            )
        if errors:
            raise ValidationError(errors)
