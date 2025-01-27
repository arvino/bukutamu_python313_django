from rest_framework import serializers
from .models import BukuTamu, Member

class BukuTamuSerializer(serializers.ModelSerializer):
    class Meta:
        model = BukuTamu
        fields = ['id', 'member', 'messages', 'gambar', 'timestamp']
        read_only_fields = ['member']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'username', 'email', 'phone', 'role']
        read_only_fields = ['role'] 