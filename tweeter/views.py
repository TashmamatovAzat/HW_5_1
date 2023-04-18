from django.shortcuts import render

from rest_framework import generics

from .models import Tweet, Comment, Mark
from .serializers import TweetSerializer, CommentSerializer, MarkSerializer


class TweetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MarkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
