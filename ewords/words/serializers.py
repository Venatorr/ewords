from rest_framework import serializers
from .models import Word


class WordsSerializers(serializers.Serializer):
    meta_user_id = serializers.IntegerField()
    meta_add_date = serializers.DateTimeField()
    rus_word = serializers.CharField()
    eng_word = serializers.CharField()
    transcription = serializers.CharField()
    picture = serializers.IntegerField()

    def create(self, validated_data):
        return Word.objects.create(**validated_data)
