from rest_framework import serializers
from .models import Word


class WordsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('meta_user', 'rus_word', 'eng_word',
                  'transcription', 'picture')
