from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

#Creiamo una vista come suggerisce il commento
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    Post.objects.get(pk=pk)
    
#abbiamo creato una funzione (def) chiamata post_list 
# che prende request e restituisce return una funzione
#  render che renderizza (mette insieme) il nostro
#  template blog/post_list.html.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})