from .models import Word, Language
from .serializers import WordsSerializers, LanguagesSerializers
from rest_framework import viewsets, status
from rest_framework.response import Response


class WordsViewset(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordsSerializers

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Word.objects.all()
        return Word.objects.filter(meta_user=user)

    def perform_create_update(self, serializer):
        serializer.save(meta_user=self.request.user)  # заменить на HiddenField в сериализаторе

    def perform_create(self, serializer):
        self.perform_create_update(serializer)

    def perform_update(self, serializer):
        self.perform_create_update(serializer)

    def create(self, request, pk=None, company_pk=None, project_pk=None):
        is_many = True if isinstance(request.data, list) else False
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LanguagesViewset(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguagesSerializers
