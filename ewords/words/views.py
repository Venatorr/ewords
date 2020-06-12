from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Word
from .serializers import WordsSerializers


class WordsView(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordsSerializers(words, many=True)
        return Response({'words': serializer.data})

    def post(self, request):
        word = request.data.get('word')
        serializer = WordsSerializers(data=word)
        if serializer.is_valid(raise_exception=True):
            word_saved = serializer.save()
        message = f'Word {word_saved.rus_word} created successfully'
        return Response({'success': message})

    def put(self, request, pk):
        print('start')
        word = get_object_or_404(Word.objects.all(), pk=pk)
        print(word)
        data = request.data.get('word')
        print(data)
        serializer = WordsSerializers(instance=word, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            word = serializer.save()
        message = f'Word "{word.rus_word} updated successfully"'
        return Response({'success': message})

    def delete(self, request, pk):
        word = get_object_or_404(Word.objects.all(), pk=pk)
        word_verbose = word.rus_word
        word.delete()
        message = f'Word "{word_verbose} deleted successfully"'
        return Response({'success': message}, status=204)
