from django.db.models import Count
from rest_framework import generics, permissions, filters,status
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from convergehub_api.permissions import IsOwnerOrReadOnly
from .models import Post,Category
from .serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class PostList(generics.GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    queryset=Post.objects.all()


    def get(self,request):
        queryset=Post.objects.all()
        postSerializer=self.get_serializer(queryset,many=True)
        return Response(postSerializer.data, status=status.HTTP_200_OK)

    def post(self, request):
    
        try:
            user=request.data['user']
            title=request.data['title']
            content=request.data['content']
            category= request.data['category']
            image=request.data['image']

            try:
                owner= User.objects.get(username=user)
            except Exception as e:
                return Response({"error":"User Not Found"},status=status.HTTP_400_BAD_REQUEST)
            try:
                category_id= Category.objects.get(name=category)
            except Exception as e:
                return Response({"error":"Category Not Found"},status=status.HTTP_400_BAD_REQUEST)
        
            post=Post.objects.create(owner=owner,title=title,content=content,category=category_id,image=image)
            post.save()

            return Response({'message': 'Successfully inserted the post to Database'}, status=status.HTTP_200_OK)


        except Exception as e:
            return Response({"error":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)

# class PostList(generics.ListCreateAPIView):
#     """
#     List posts or create a post if logged in
#     The perform_create method associates the post with the logged in user.
#     """
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.annotate(
#         likes_count=Count('likes', distinct=True),
#         comments_count=Count('comment', distinct=True)
#     ).order_by('-created_at')
#     filter_backends = [
#         filters.OrderingFilter,
#         filters.SearchFilter,
#         DjangoFilterBackend,
#     ]
#     filterset_fields = [
#         'owner__followed__owner__profile',
#         'likes__owner__profile',
#         'owner__profile',
#     ]
#     search_fields = [
#         'owner__username',
#         'title',
#     ]
#     ordering_fields = [
#         'likes_count',
#         'comments_count',
#         'likes__created_at',
#     ]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


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