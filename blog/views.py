from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsAdminUserOrReadOnly, IsContentCreatorUserOrManagerReadOnly
from .serializers import CustomTokenObtainPairSerializer, BlogSerializer, UserSerializer
from .models import CustomUser, Blog


class CustomTokenObtainPairView(generics.GenericAPIView):
    serializer_class = CustomTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user = CustomUser.objects.get(id=user["id"])
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
        })
        
class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
   
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsContentCreatorUserOrManagerReadOnly)
   
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsContentCreatorUserOrManagerReadOnly)

