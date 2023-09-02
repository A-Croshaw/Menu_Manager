from django.views.generic import TemplateView

class Index(TemplateView):
    """ Render home page """
    template_name = 'home/index.html'
