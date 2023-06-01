from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'about_us.html'
