from rest_framework.generics import get_object_or_404
from .models import Word, User
from .serializers import WordsSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class WordsView(ListModelMixin, GenericAPIView, CreateModelMixin):
    queryset = Word.objects.all()
    serializer_class = WordsSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('meta_user'))
        return serializer.save(meta_user=user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
