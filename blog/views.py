from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.edit import FormView

from blog.forms import BlogForm, BlogModelForm
from .models import Blog, Entry

# Create your views here.

class BlogsListView (View):
    def get(self, request):
        blogs = Blog.objects.all()
        context={
            'blogs':blogs
        }
        return render(request, 'blog/blogs_list.html', context)


class EntryListView (View):
    def get(self, request, pk, *args, **kwargs):
        entries = Entry.objects.filter(blog=pk)
        context={
            'entries':entries,
        }
        name_blog = Blog.objects.get(pk=pk)
        context_pk={
            'name_blog':name_blog
        }
        new_context={**context, **context_pk}
        return render(request, 'blog/entry_list.html', new_context)


class EntryDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        entry = get_object_or_404(Entry, pk=pk)
        
        context = {
            'entry':entry
        }
        name_blog = Blog.objects.get(pk=pk)
        context_pk={
            'name_blog':name_blog
        }
        new_context={**context, **context_pk}
        return render(request, 'blog/entry_detail.html', new_context)


class EntryFormView(FormView):
    template_name = 'blog/blog_create.html'
    form_class = BlogModelForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def post_create(request):
    #con forms.Form
    """
    form = BlogForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        tagline = form.cleaned_data.get('tagline')
        blog = Blog(name=name, tagline=tagline)
        blog.save()
        return redirect("Blog:home")
    """

    #con forms.ModelForm
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("Blog:home")


    context = {
        'form':form
    }
    return render(request, 'blog/blog_create.html', context)

