from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from api_v1.serializers import NoteSeriallzer
from notes.models import Note

class NoteListView(generics.ListAPIView):
    # 使用JWT Token
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSeriallzer

class NoteDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Note.objects.all()
    serializer_class = NoteSeriallzer

class NoteCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Note.objects.all()
    serializer_class = NoteSeriallzer

class NoteRouterView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return NoteListView.as_view()(request, *args, **kwargs)
        if request.method == "POST":
            return NoteCreateView.as_view()(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)