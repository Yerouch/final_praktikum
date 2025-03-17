from django.contrib import admin
from django.urls import path, include
from polls.models import Choice
from workorder_project.models import Workorder, Notification, User, Approval, Role
from rest_framework import routers, serializers, viewsets

#  Choice
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes']

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

# User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['userid', 'displayname', 'department']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Workorder
class WorkorderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workorder
        fields = [
            'workorderid',
            'description',
            'startdate',
            'enddate',
            'status',
            'results',
            'priority',
            'responsible'
        ]

class WorkorderViewSet(viewsets.ModelViewSet):
    queryset = Workorder.objects.all()
    serializer_class = WorkorderSerializer

# Approval
class ApprovalSerializer(serializers.HyperlinkedModelSerializer):
    userid = serializers.PrimaryKeyRelatedField(read_only=True)
    workorderid = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Approval
        fields = ['approvalid', 'userid', 'workorderid', 'status']

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer

# Role
class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['roleid', 'rolename', 'permissionlevel', 'users']

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Notification
class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['notificationid', 'text', 'date', 'workorderid', 'roles']

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'workorder', WorkorderViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'user', UserViewSet)
router.register(r'approval', ApprovalViewSet)
router.register(r'role', RoleViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
