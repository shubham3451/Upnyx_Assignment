from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer
from django.contrib.auth import authenticate
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            User.objects.create(username=username, password=make_password(password))
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework_simplejwt.tokens import RefreshToken

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

class ChatAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get('message')
        if not message:
            return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if user.tokens < 100:
            return Response({'error': 'Insufficient tokens'}, status=status.HTTP_400_BAD_REQUEST)

        response_text = "This is a Dummy Response"
        user.tokens -= 100
        user.save()

        chat = Chat.objects.create(
            user=user,
            message=message,
            response=response_text,
            timestamp=timezone.now()
        )
        
        serializer = ChatSerializer(chat)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TokenBalanceAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'tokens': user.tokens}, status=status.HTTP_200_OK)


