from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Topic


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок статьи')
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        label='Тема',
        widget=forms.widgets.Select(attrs={'size': 3}),
        required=False
        )
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    comment = forms.CharField(label='Комментарий', required=False)

    class Meta:
        model = Post
        fields = ('title', 'topic', 'content', 'comment')

    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['title']:
            errors['content'] = ValidationError(
                'Укажите описание продаваемого товара'
            )
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError(
                'Укажите описание продаваемого товара'
            )
        if errors:
            raise ValidationError(errors)

        return self.cleaned_data
