from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from blogs.models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
def index(request):
    return render (request,"blogs/index.html")

class BlogCreateView(CreateView):
    model = Posts
    fields = ["Title","Content","Date_Of_Upload","Image"]
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class BlogListView(ListView):
    model = Posts

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Posts

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Posts
    fields = ["Title","Content","Image"]
    template_name = "blogs/posts_update.html"
    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Posts
    success_url = "/"
