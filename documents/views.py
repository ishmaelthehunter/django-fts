from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Document
from .forms import DocumentSearchForm

def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DocumentSearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            search_results = Document.objects.search(form.cleaned_data['search_term'])
            return render(request, 'search_results.html', {'documents': search_results, 'search_term': form.cleaned_data['search_term']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DocumentSearchForm()

    return render(request, 'search.html', {'form': form})
