from . models import Genre, Book
from . forms import CreateGenreForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
    




class Test(TemplateView):
    template_name = 'testapp/test/html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context['rate'] = self.get_rate()
        return context

    def get_rate(self):
        return 2.776   
class CreateGenre(CreateView):
    model = Genre
    form_class = CreateGenreForm
    temlate_name = 'testapp/create_genre/html'
    success_url ="/list-genre/"
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['rate'] = 123
    #    return context
class UpdateGenre(UpdateView):
    model = Genre
    form_class = CreateGenreForm
    temlate_name = 'testapp/create_genre.html'
    success_url = "/list-genre/"
 
class ListGenre(ListView):
    model = Genre
    temlate_name = 'testapp/list_genre.html'
    success_url = "/list-genre/"
    
  
class DeleteGenre(DeleteView):
    model = Genre
    temlate_name = 'testapp/delete_genre.html'
    success_url = "/list-genre/"
  