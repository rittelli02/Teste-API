from django.contrib import admin 
from django.urls import path , include
from core.views import UserViewSet, ProjViewSet, GerViewSet
from rest_framework import routers  
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = routers.DefaultRouter()
router.register(r'usuario', UserViewSet)
router.register(r'projeto',ProjViewSet)
router.register(r'gerenciamento', GerViewSet)

urlpatterns = [
    #path('api-token-auth/', obtain_jwt_token),
    
    #path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
