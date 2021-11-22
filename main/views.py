from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import CodeImageSerializer, ProblemSerializer, ReplySerializer, CommentSerializer


# class ProblemListView(ListAPIView):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemListSerializer
#
#
# class ProblemCreateView(CreateAPIView):
#     queryset = Problem
#     serializer_class = ProblemCreateSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# class CodeImageView(ListAPIView):
#     queryset = CodeImage.objects.all()
#     serializer_class = CodeImageSerializer
#
#     def get_serializer_context(self):
#         context= super.get_serializer_context()
#         context['request'] = self.request
#         return context

class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
