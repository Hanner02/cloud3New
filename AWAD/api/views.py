from django.shortcuts import render
from rest_framework import generics, viewsets
from api.models import ReviewItem
from .serializers import ReviewSerializer
    

class ReviewList(generics.ListCreateAPIView):
    queryset = ReviewItem.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewItem.objects.all()
    serializer_class = ReviewSerializer

    