from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from categories.models import Category
from convergehub_api.permissions import IsOwnerOrReadOnly

from .models import Post
from .serializers import CategorySerializer, PostSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostList(generics.GenericAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [AllowAny]

    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'category',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def get(self,request):
        queryset=Post.objects.all()
        postSerializer=self.get_serializer(queryset,many=True)
        return Response(postSerializer.data, status=status.HTTP_200_OK)

    def post(self, request):
    
        try:
            user=request.user

            title=request.data['title']
            image=request.data['image']

            content=request.data['content']
            category= request.data['category']

            category_id=Category.objects.get(slug=category)
            post=Post.objects.create(owner=user,title=title,content=content,category=category_id,image=image)
            post.save()
            return Response({'message': 'Successfully inserted the post to Database'}, status=status.HTTP_200_OK)


        except Exception as e:
            return Response({"error":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        category = get_object_or_404(Category, id=self.request.data.get('category'))
        serializer.save(category=category)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')