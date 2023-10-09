from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # jwt 토큰
        access_token = 'test' # str(RefreshToken.for_user(user).access_token)

        return Response({'access_token': access_token, **serializer.data}, status=status.HTTP_201_CREATED,
                        headers=(self.get_success_headers(serializer.data)))
