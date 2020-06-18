from .models import Word, Language, User
from .serializers import WordsSerializers, LanguagesSerializers, UserSerializers
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import make_password


class WordsViewset(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordsSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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
    # permission_classes = (permissions.IsAuthenticated, )


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):  # в рабочей версии убрать get, он не нужен
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response({'users': serializer.data})

    def get_token(self, data):
        user = User.objects.get(username=data['username'])
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        data['token'] = token
        return data

    def post(self, request):
        user = request.data
        user['password'] = make_password(user['password'])
        serializer = UserSerializers(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = self.get_token(serializer.data)
        return Response(response, status=status.HTTP_201_CREATED)
