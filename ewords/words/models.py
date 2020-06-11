from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Word(models.Model):
    meta_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    meta_add_date = models.DateTimeField(auto_now_add=True, null=False)
    rus_word = models.TextField(null=False, blank=False)
    eng_word = models.TextField(null=False, blank=False)
    transcription = models.TextField(null=True, blank=True)
    picture = models.IntegerField(null=True, blank=True)
