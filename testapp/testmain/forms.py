from django import forms
from models import UploadFileModel


class UploadForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    file = forms.FileField()


class UploadModelForm(forms.ModelForm):

    class Meta:
        model = UploadFileModel
