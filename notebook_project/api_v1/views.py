from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema
from api_v1.serializers import NoteSerializer
from notes.models import Note

class NoteViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="取得 單一筆 Note詳細內容",
        description="根據 Note 的主鍵取得詳細資訊",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="取得 Note清單",
        description="取得 Note清單",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="建立 Note",
        description="覆蓋 POST 的認證為 AllowAny",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)