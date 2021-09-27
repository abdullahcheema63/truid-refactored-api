from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *


class UploadFaceFrame(CreateAPIView):
    serializer_class = FaceFrameSerializer


class UploadReferenceFrame(CreateAPIView):
    serializer_class = ReferenceFrameSerializer


class UploadAgentFrame(CreateAPIView):
    serializer_class = AgentFrameSerializer


class UploadAuthenticationFrame(CreateAPIView):
    serializer_class = AuthenticationFrameSerializer


class IDToSelfieMatchingView(APIView):
    serializer_class = IDToSelfieSerializer

    def post(self, request, format=None):
        serializer = IDToSelfieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
