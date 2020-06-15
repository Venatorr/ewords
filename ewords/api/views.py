from rest_framework.generics import get_object_or_404
from .models import Word, User
from .serializers import WordsSerializers
from rest_framework import viewsets


class WordsViewset(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordsSerializers

