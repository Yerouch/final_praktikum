from rest_framework import generics
from workorder_project.models import User, Workorder, Approval, Role, Notification
from workorder_project.urls import UserSerializer, WorkorderSerializer, ApprovalSerializer, RoleSerializer, NotificationSerializer


# User
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Workorder
class WorkorderListCreateView(generics.ListCreateAPIView):
    queryset = Workorder.objects.all()
    serializer_class = WorkorderSerializer


class WorkorderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workorder.objects.all()
    serializer_class = WorkorderSerializer


# Approval
class ApprovalListCreateView(generics.ListCreateAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer


class ApprovalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer


# Role
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# Notification
class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer