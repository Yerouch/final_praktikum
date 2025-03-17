from django.contrib import admin

from .models import Workorder, Notification, User, Approval, Role

admin.site.register(Workorder)
admin.site.register(Notification)
admin.site.register(User)
admin.site.register(Approval)
admin.site.register(Role)
