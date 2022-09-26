from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import BrandViewSet, ColorPaletteViewSet, UserProfileViewSet, create_brand

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'colorpalette', ColorPaletteViewSet)
router.register(r'user_profile', UserProfileViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/brands/create', create_brand, name='create_brand'),
]
