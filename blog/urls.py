from django.urls import path
from .views import BlogsListView, EntryDetailView, EntryListView, post_create, EntryFormView

app_name = 'Blog'

urlpatterns = [
    path('', BlogsListView.as_view(), name='home'),
    #path('create/', post_create, name='blog_create'),
    path('create/', EntryFormView.as_view(), name='blog_create'),
    path('<int:pk>/', EntryListView.as_view(), name='entry_list'),
    path('entry<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
]