from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('upload-face-frame',views.UploadFaceFrame.as_view()),
    path('upload-reference-frame',views.UploadReferenceFrame.as_view()),
    path('upload-agent-frame',views.UploadAgentFrame.as_view()),
    path('upload-authentication-frame',views.UploadAuthenticationFrame.as_view()),
    path('id-to-selfie-matching',views.IDToSelfieMatchingView.as_view())
]

