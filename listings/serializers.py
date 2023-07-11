from rest_framework import serializers
from .models import Listings, ListingPhoto

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms','sqft', 'photo_main', 'slug')

class ListingPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingPhoto
        fields = ['photo']

class ListingDetailSerializer(serializers.ModelSerializer):
    # images = ListingPhotosSerializer(many = True)
    class Meta:
        model = Listings
        fields = '__all__'
        lookup_field = 'slug'
