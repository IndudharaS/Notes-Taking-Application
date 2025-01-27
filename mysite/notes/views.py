from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import NotesForm
from django.http import *

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    context_object_name = 'notes'
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes' 
    form_class = NotesForm
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title','text']
    success_url = '/smart/notes' 
    form_class = NotesForm
    login_url = '/login'

    # def get_queryset(self):
    #     return self.request.user.notes.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    # template_name = 'notes/list.html'         It can be ignored
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

# def deatail(request,pk):
#     note = Notes.objects.get(pk=pk)
#     return render(request,'notes/notes_details.html',{'note':note})
