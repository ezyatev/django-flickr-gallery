from ckeditor.widgets import CKEditorWidget
from django import forms

from example.myapp.models import Article


class ArticleAdminForm(forms.ModelForm):

    class Meta:
        model = Article
        widgets = {
            'content': CKEditorWidget
        }
