from rest_framework import serializers
from .models import ReviewItem

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewItem
        fields = '__all__'