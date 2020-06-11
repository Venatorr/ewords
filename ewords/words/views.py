from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Word
from .serializers import WordsSerializers


class WordsView(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordsSerializers(words, many=True)
        return Response({'words': serializer.data})

    def post(self, request):
        word = request.data.get('word')
        print(word)
        serializer = WordsSerializers(data=word)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            word_saved = serializer.save()
        print(word)
        return Response({'success': f'Word {word_saved.rus_word} created successfully'})
