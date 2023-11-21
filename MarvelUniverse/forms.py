from .models.comment_models import SeriesComment, ComicComment, CharacterComment
from django import forms


class SeriesCommentForm(forms.ModelForm):
    class Meta:
        model = SeriesComment
        fields = ['user_comment']

class ComicCommentForm(forms.ModelForm):
    class Meta:
        model = ComicComment
        fields = ['user_comment']

class CharacterCommentForm(forms.ModelForm):
    class Meta:
        model = CharacterComment
        fields = ['user_comment']
