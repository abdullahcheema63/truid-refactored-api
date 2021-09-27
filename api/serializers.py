from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import *


class FaceFrameSerializer(serializers.ModelSerializer):
    session = serializers.PrimaryKeyRelatedField(required=False, queryset=Session.objects.all())

    class Meta:
        model = FaceFrame
        fields = '__all__'

    def create(self, validated_data):
        if 'session' not in validated_data:
            session = Session()
            session.save()
            validated_data['session'] = session
            return FaceFrame.objects.create(**validated_data)
        else:
            try:
                session = validated_data['session']
                faceframe = session.faceframe
                faceframe.image = validated_data['image']
                faceframe.save()
                return faceframe
            except ObjectDoesNotExist:
                return FaceFrame.objects.create(**validated_data)


class ReferenceFrameSerializer(serializers.ModelSerializer):
    session = serializers.PrimaryKeyRelatedField(required=False, queryset=Session.objects.all())

    class Meta:
        model = ReferenceFrame
        fields = '__all__'

    def create(self, validated_data):
        if 'session' not in validated_data:
            session = Session()
            session.save()
            validated_data['session'] = session
            return ReferenceFrame.objects.create(**validated_data)
        else:
            try:
                session = validated_data['session']
                reference_frame = session.referenceframe
                reference_frame.image = validated_data['image']
                reference_frame.save()
                return reference_frame
            except ObjectDoesNotExist:
                return ReferenceFrame.objects.create(**validated_data)


class AgentFrameSerializer(serializers.ModelSerializer):
    session = serializers.PrimaryKeyRelatedField(required=False, queryset=Session.objects.all())

    class Meta:
        model = AgentFrame
        fields = '__all__'

    def create(self, validated_data):
        if 'session' not in validated_data:
            session = Session()
            session.save()
            validated_data['session'] = session
            return AgentFrame.objects.create(**validated_data)
        else:
            try:
                session = validated_data['session']
                agent_frame = session.agentframe
                agent_frame.image = validated_data['image']
                agent_frame.save()
                return agent_frame
            except ObjectDoesNotExist:
                return AgentFrame.objects.create(**validated_data)


class AuthenticationFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentFrame
        fields = '__all__'

    def create(self, validated_data):
        # TODO: work on authentication frame here (using classes and functions only)
        return AuthenticationFrame.objects.create(**validated_data)


class IDToSelfieSerializer(serializers.Serializer):
    session = serializers.PrimaryKeyRelatedField(required=True, queryset=Session.objects.all())
    status = serializers.BooleanField(read_only=True)

    def validate(self, data):
        session = data['session']
        ref_frame = None
        face_frame = None
        try:
            ref_frame = session.referenceframe
        except ObjectDoesNotExist:
            raise ValidationError("session does not have reference frame ")
        try:
            face_frame = session.faceframe
        except ObjectDoesNotExist:
            raise ValidationError("session does not have face frame ")
        if ref_frame is not None and face_frame is not None:
            return data
        else:
            raise ValidationError("session does not have face frame or reference frame")

    def create(self, validated_data):
        # TODO: calculate id selfie status (using classes and functions only)
        validated_data['status'] = True
        return validated_data
