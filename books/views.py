from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import (
    Book,
    Author,
    IndustryIdentifiers,
)
from .forms import (
    BookForm,
    AuthorForm,
    IdentifiersForm,
)


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    paginate_by = 10


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/create.html'
    form_class = BookForm
    success_url = 'list'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'books/author.html'
    form_class = AuthorForm
    success_url = 'create'


class IdentifiersCreateView(CreateView):
    model = IndustryIdentifiers
    template_name = 'books/identifiers.html'
    form_class = IdentifiersForm
    success_url = 'create'
