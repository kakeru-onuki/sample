from django import forms
from .models import Article
from .models import Document

class SearchForm(forms.Form):
    keyword=forms.CharField(label="Sercharticle",max_length=100)
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=("content","user_name")
# -------------------------------
class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=("description","photo",)
