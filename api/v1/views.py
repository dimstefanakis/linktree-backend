import os
import json
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes)
from accounts.models import UserProfile
from brand.models import Brand, ColorPalette
from . import serializers


class BrandViewSet(viewsets.ModelViewSet):
    model = Brand
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [AllowAny]
    lookup_field = "username"


class ColorPaletteViewSet(viewsets.ModelViewSet):
    model = ColorPalette
    queryset = ColorPalette.objects.all()
    serializer_class = serializers.ColorPaletteSerializer
    permission_classes = [AllowAny]


class UserProfileViewSet(viewsets.ModelViewSet):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [AllowAny]


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def create_brand(request):
    data = request.data.copy()
    color_palette_data = data.pop('color_palette')[0]
    color_palette = json.loads(color_palette_data)
    data['color_palette'] = color_palette
    color_palette_serializer = serializers.ColorPaletteSerializer(
        data=data['color_palette'])

    if color_palette_serializer.is_valid():
        color_palette_serializer.save()
        color_palette = ColorPalette.objects.get(
            id=color_palette_serializer.data['id'])
    else:
        return Response({'errors': color_palette_serializer.errors})

    serializer = serializers.BrandSerializer(data=data)
    if serializer.is_valid():
        brand = serializer.save()
        brand.color_palette = color_palette
        brand.save()
        return Response(serializer.data)

    return Response({'errors': serializer.errors})
