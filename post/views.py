from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView


class PostListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.method == "GET":
            post_qs = Post.objects.all()
            serializer = PostSerializer(instance=post_qs, many=True)
            data = serializer.data
            return Response(data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        if request.method == "GET":
            post = self.get_object(pk)
            serializer = PostDetailSerializer(post)
            data = serializer.data
            return Response(data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostDetailSerializer(post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_pk):
        return get_object_or_404(Post, pk=post_pk)

    def get(self, request, post_pk):
        post = self.get_object(post_pk)
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_pk):
        post = self.get_object(post_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def post_list(request):
#     if request.method == "GET":
#         post_qs = Post.objects.all()
#         serializer = PostSerializer(instance=post_qs, many=True)
#         data = serializer.data
#         return Response(data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "DELETE"])
# def post_detail(request, pk):
#     if request.method == "GET":
#         post = get_object_or_404(Post, pk=pk)
#         serializer = PostSerializer(post)
#         data = serializer.data
#         return Response(data)

#     elif request.method == "PUT":
#         post = get_object_or_404(Post, pk=pk)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     elif request.method == "DELETE":
#         post = get_object_or_404(Post, pk=pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
