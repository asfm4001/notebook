from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from notes.models import Note
from notes.forms import NoteForm
# Create your views here.
class NoteListView(generic.ListView):
    model = Note
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "筆記"
        return context
    # template_name = "notes/list.html"

# def noteDetail(request, note_id):
#     note = Note.objects.filter(pk=note_id)
#     return render(request, '')
class NoteDetailView(generic.DetailView):
    model = Note
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_object().title
        return context

class NoteCreateView(generic.CreateView):
    model = Note
    fields = ["title", "content"]
    # template_name = "create_note_form.html"
    success_url = reverse_lazy('note:list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新增筆記"
        return context
    # def get_success_url(self):
    #     return reverse('note:list')

    # form_class = NoteForm
    # template_name = "notes/new.html"