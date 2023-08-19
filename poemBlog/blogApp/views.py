from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "blogApp/index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

#render a single post.    
def post_single(request, post):
     post = get_object_or_404(Post, slug=post, status="published")
     return render(request, "blogApp/single.html", {"post":post})