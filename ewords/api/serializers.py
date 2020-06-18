from rest_framework import serializers
from .models import Word, Language, User


class LanguageField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Language.objects.get(name=data)


class WordsSerializers(serializers.ModelSerializer):
    language = LanguageField(queryset=Language.objects.all())
    meta_user = serializers.CharField(max_length=100)

    class Meta:
        model = Word
        fields = ('id', 'meta_user', 'meta_add_date', 'rus_word',
                  'eng_word', 'transcription', 'picture', 'language')
        read_only_fields = ('id', 'meta_add_date', )


class LanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')
        read_only_fields = ('id',)


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)
        # для удобства тестирования пароль отображается, но затем надо будет раскомментировать
        # следующую строку и оставить его write_only
        # extra_kwargs = {'password': {'write_only': True}}
