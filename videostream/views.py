# from pytube import YouTube
from rest_framework import generics, mixins, status, viewsets
from django.shortcuts import render , get_object_or_404
from .models import Video
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import VideoSerializer

class VideoDetails(generics.GenericAPIView):
    """
	A Generic API that returns Videos by date
	"""
    serializer_class = VideoSerializer
    def get_queryset(self):
        try:
       	    video_obj = Video.objects.filter()
        except Video.DoesNotExist:
	        video_obj = None
        if not video_obj:
	        return {'Error': 'Videos Do Not Exist'}
        else:
	        serializer = VideoSerializer(video_obj, many=True)
        return serializer.data

    def get(self, request, pk=None):
    	return Response(self.get_queryset())
