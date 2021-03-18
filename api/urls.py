from django.contrib import admin 
from django.urls import path , include
from core.views import UserViewSet, ProjViewSet, GerViewSet
from rest_framework import routers  
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register(r'usuario', UserViewSet)
router.register(r'projeto',ProjViewSet)
router.register(r'gerenciamento', GerViewSet)

urlpatterns = [
    #path('api-token-auth/', obtain_jwt_token),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
