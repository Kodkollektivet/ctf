from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse_lazy
from . import models


class Question(CreateView):
    model = models.Answer
    fields = ['answer']
    answer = ''  # Override this
    success_url = reverse_lazy('index')  # Point to next question

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if form.is_valid():
            if form.data.get('answer') == self.answer:
                return self.form_valid(form)

        form.add_error(None, 'Sorry!')
        return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form
        return super(ModelFormMixin, self).form_valid(form)


class Index(TemplateView):
    template_name = 'ctf/base.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['doneit'] = models.DoneIt.objects.all()
        return context


class VadFinnsGjomtIKoden(Question):
    """Vad finns gjomt i koden?"""
    template_name = 'ctf/vad-finns-gjomt-i-koden.html'
    answer = 'matematik'
    success_url = reverse_lazy('ctf:matematik')  # Next question


class Matematik(Question):
    """Matematik"""
    template_name = 'ctf/matematik.html'
    answer = '274877906944'
    success_url = reverse_lazy('ctf:kryptering')  # Next question


class Kryptering(Question):
    """Kryptering"""
    template_name = 'ctf/kryptering.html'
    answer = 'networking'
    success_url = reverse_lazy('ctf:the_end')  # Next question


class TheEnd(CreateView):
    model = models.DoneIt
    fields = ['first_name', 'last_name']
    template_name = 'ctf/the_end.html'
    success_url = reverse_lazy('index')
