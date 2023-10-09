from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # TODO: 퍼미션 관련 구현
    # permission_classes = [permissions.IsAuthenticated]

    def get_access_token(self, user):
        # jwt 토큰 생성
        return str(RefreshToken.for_user(user).access_token)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers={
            'Authorization': f'Bearer {self.get_access_token(user)}',
            **self.get_success_headers(serializer.data)
        })

    @action(detail=False, methods=['post'])
    def login(self, request):
        user = authenticate(username=(request.data.get('username')), password=(request.data.get('password')))

        if user:
            return Response({}, status=status.HTTP_200_OK, headers={
                'Authorization': f'Bearer {self.get_access_token(user)}'
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)