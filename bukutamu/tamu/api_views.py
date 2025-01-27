from rest_framework import viewsets, permissions
from .models import BukuTamu, Member
from .serializers import BukuTamuSerializer, MemberSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.role == 'admin'

class BukuTamuViewSet(viewsets.ModelViewSet):
    queryset = BukuTamu.objects.all()
    serializer_class = BukuTamuSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return BukuTamu.objects.all()
        return BukuTamu.objects.filter(member=self.request.user)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.filter(role='member')
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly] 