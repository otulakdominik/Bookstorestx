from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.db.models import Q
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


class SearchResultsView(ListView):
    model = Book
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(language__icontains=query) | Q(authors__name__icontains=query)
        )

        return object_list


class DataSearchResultsView(ListView):
    model = Book
    template_name = 'books/search_results.html'

    def get_queryset(self):
        start = self.request.GET.get('s')
        end = self.request.GET.get('e')
        object_list = Book.objects.filter(released__range=[start, end])

        return object_list
