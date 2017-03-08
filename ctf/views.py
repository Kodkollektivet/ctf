from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from . import models


class Index(TemplateView):
    template_name = 'ctf/base.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['doneit'] = models.DoneIt.objects.all()
        return context


class VadFinnsGjomtIKoden(TemplateView):
    """Vad finns gjomt i koden?"""
    template_name = 'ctf/vad-finns-gjomt-i-koden.html'


class Matematik(TemplateView):
    """Matematik"""
    template_name = 'ctf/matematik.html'


class Kryptering(TemplateView):
    """Kryptering"""
    template_name = 'ctf/kryptering.html'


class TheEnd(CreateView):
    model = models.DoneIt
    fields = ['first_name', 'last_name']
    template_name = 'ctf/the_end.html'
    success_url = reverse_lazy('index')
