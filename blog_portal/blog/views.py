from django.shortcuts import render, get_object_or_404
from .models import Blog
from .serializers import BlogSerializer, DetailedBlogSerializer
from rest_framework.response import Response
from rest_framework import status, generics

def blog_list(request):
    blogs = Blog.objects.filter(published=True)
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, published=True)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'Message': 'Blog created'}, status = status.HTTP_201_CREATED)
    
class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = DetailedBlogSerializer