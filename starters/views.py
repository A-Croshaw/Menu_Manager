from django.views.generic import ListView
from django.db.models import Q
from .models import Starter


class ViewStarter(ListView):
    """View All starters"""

    template_name = "starters/starters.html"
    context_object_name = "starters"
    model = Starter

    def get_queryset(self, **kwargs):
        """
        Starter search function
        """
        starter_search = self.request.GET.get('q')
        if starter_search:
            starter = self.model.objects.filter(
                Q(starter_name__icontains=starter_search) |
                Q(starter_type__icontains=starter_search)
            )
        else:
            starter = self.model.objects.all()
        return starter