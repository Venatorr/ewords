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

    def update(self, instance, validated_data):
        instance.meta_user_id = validated_data.get('meta_user_id',
                                                   instance.meta_user_id)
        instance.meta_add_date = validated_data.get('meta_add_date',
                                                    instance.meta_add_date)
        instance.rus_word = validated_data.get('rus_word', instance.rus_word)
        instance.eng_word = validated_data.get('eng_word', instance.eng_word)
        instance.transcription = validated_data.get('transcription',
                                                    instance.transcription)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.save()
        return instance
