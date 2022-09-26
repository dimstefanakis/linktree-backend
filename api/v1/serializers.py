from rest_framework import serializers
from brand.models import Brand, ColorPalette
from accounts.models import UserProfile


class ColorPaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorPalette
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    color_palette = ColorPaletteSerializer(read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'
