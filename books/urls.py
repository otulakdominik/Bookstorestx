from . import views
from django.urls import path


app_name = 'books'

urlpatterns = [
    path('list', views.BookListView.as_view(), name='list'),
    path('create', views.BookCreateView.as_view(), name='create'),
    path('create_author', views.AuthorCreateView.as_view(), name='create_author'),
    path('create_identifiers', views.IdentifiersCreateView.as_view(), name='create_identifiers'),
]
