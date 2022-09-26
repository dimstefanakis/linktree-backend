from django.db import models

class ColorPalette(models.Model):
    background_color = models.CharField(max_length=100, default='#ffffff')
    text_color = models.CharField(max_length=100, default='#000000')
    link_color = models.CharField(max_length=100, default='#0077ff')
    button_color = models.CharField(max_length=100, default='#000000')
    button_text_color = models.CharField(max_length=100, default='#ffffff')

class Brand(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=40, unique=True, blank=True, default='')
    intro = models.TextField()
    mission = models.TextField()
    logo = models.ImageField(upload_to='brand/logo')
    font = models.CharField(max_length=100, null=True, blank=True)
    color_palette = models.ForeignKey(ColorPalette, on_delete=models.CASCADE, null=True, related_name="brand")
    website_url = models.URLField(max_length=200, null=True, blank=True)
    facebook_url = models.URLField(max_length=200, null=True, blank=True)
    twitter_url = models.URLField(max_length=200, null=True, blank=True)
    instagram_url = models.URLField(max_length=200, null=True, blank=True)
    youtube_url = models.URLField(max_length=200, null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
