from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import (
    CustomTokenObtainPairView,
    
    UserList,
    UserDetail,
    BlogList,
    BlogDetail,
)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/blogs/', BlogList.as_view(), name='blog-list'),
    path('api/blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
]
