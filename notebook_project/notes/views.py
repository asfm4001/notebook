from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from notes.models import Note
from notes.forms import NoteForm
# Create your views here.
class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "筆記"
        return context

class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_object().title
        return context

class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    # fields = ["title", "content"]
    form_class = NoteForm
    # template_name = "create_note_form.html"
    success_url = reverse_lazy("note:list")
    def form_valid(self, form):
        # form.instance: 未被儲存的新物件 or 編輯中的物件
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新增筆記"
        return context