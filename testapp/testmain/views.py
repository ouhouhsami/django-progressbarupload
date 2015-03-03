# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from testmain.forms import UploadForm, UploadModelForm


def upload_modelform(request):
    if request.method == 'POST':
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/testapp/modelform')
    else:
        form = UploadModelForm()
    return render(request, 'testmain/form.html', {'form': form})