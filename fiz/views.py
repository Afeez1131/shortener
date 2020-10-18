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
        if form.is_valid():
            new_url = form.cleaned_data['url']
            obj, created = fizzURL.objects.get_or_create(url=new_url)
            context = {
                'obj': obj,
                'created': created,
            }
            if created:
                template = 'fiz/created.html'
            
            else:
                template= 'fiz/already-exist.html'

        return render(request, template, context)

class FizCBV(View):
    def get(self, request, shortcode):
        obj = get_object_or_404(fizzURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
