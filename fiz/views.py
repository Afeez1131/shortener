from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import fizzURL
from django.views import View
from fiz.utils import create_shortcode
from .forms import SubmitURLForm

class HomeView(View):
    '''
    for a CBV, post and get function will be written separately, unlike 
    FBV which handles the two by itself
    '''
    def get(self, request):
        form = SubmitURLForm
        return render(request, 'fiz/home.html', {'form': form, 'title': 'Fiz.co'})

    def post(self, request):
        form = SubmitURLForm(request.POST)
        # print(form.clean())
        return render(request, 'fiz/home.html', {'form': form, 'title': 'Fiz.co'})

class FizCBV(View):
    def get(self, request, shortcode=None):
        url = request.POST
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url 
        shortcode = code_generator(url) 
        return HttpResponseRedirect(url)
