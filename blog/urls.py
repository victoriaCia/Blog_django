from django.urls import path, include
from .views import BlogsListView, EntryDetailView, EntryListView, PostsListView, EntryFormView, search_bar, sign_up

app_name = 'Blog'

urlpatterns = [
    path('', BlogsListView.as_view(), name='home'),
    path('',include('django.contrib.auth.urls')),
    path('posts/', PostsListView.as_view(), name='posts_list'),
    #path('create/', post_create, name='blog_create'),
    path('create/', EntryFormView.as_view(), name='blog_create'),
    path('<int:pk>/', EntryListView.as_view(), name='entry_list'),
    path('entry<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('register/', sign_up, name='sign_up'),
    path('results/', search_bar, name='search_results'),
]