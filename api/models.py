from django.db import models


# Create your models here.

class Agent(models.Model):
    name = models.CharField(null=False, blank=False, max_length=250)
    image = models.ImageField(null=False, blank=False, upload_to="agents")


class Session(models.Model):
    agent = models.ForeignKey(Agent, blank=True, null=True, related_name="session", on_delete=models.CASCADE)
    report = models.JSONField(default=dict,blank=True,null=True)


class AgentFrame(models.Model):
    image = models.ImageField()
    session = models.OneToOneField(Session, on_delete=models.CASCADE)


class FaceFrame(models.Model):
    image = models.ImageField()
    session = models.OneToOneField(Session, on_delete=models.CASCADE)


class ReferenceFrame(models.Model):
    image = models.ImageField()
    session = models.OneToOneField(Session, on_delete=models.CASCADE)


class AuthenticationFrame(models.Model):
    image = models.ImageField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='authentication_frames')
