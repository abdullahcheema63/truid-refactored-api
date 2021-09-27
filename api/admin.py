from django.contrib import admin
from .models import *


# Register your models here.

class FaceFrameInline(admin.StackedInline):
    model = FaceFrame


class ReferenceFrameInline(admin.StackedInline):
    model = ReferenceFrame


class AuthenticationFramesInline(admin.StackedInline):
    model = AuthenticationFrame


class AgentFrameInline(admin.StackedInline):
    model = AgentFrame


class SessionAdmin(admin.ModelAdmin):
    inlines = (FaceFrameInline, ReferenceFrameInline, AuthenticationFramesInline, AgentFrameInline)


admin.site.register(Session, SessionAdmin)
admin.site.register(Agent)
