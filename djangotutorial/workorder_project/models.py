import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
    userid = models.IntegerField(unique=True, primary_key=True)
    displayname = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class Workorder(models.Model):
    workorderid = models.IntegerField(unique=True, primary_key=True)
    description = models.CharField(max_length=200)
    startdate = models.DateTimeField("Start date")
    enddate = models.DateTimeField("End date")
    status = models.CharField(max_length=30)
    results = models.CharField(max_length=200)
    priority = models.CharField(max_length=30)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)

class Approval(models.Model):
    approvalid = models.IntegerField(unique=True, primary_key=True)
    status = models.CharField(max_length=100)
    workorderid = models.ForeignKey(Workorder, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

class Role(models.Model):
    roleid = models.IntegerField(unique=True, primary_key=True)
    rolename = models.CharField(max_length=100)
    permissionlevel = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='users')

class Notification(models.Model):
    notificationid = models.IntegerField(unique=True, primary_key=True)
    text = models.CharField(max_length=200)
    date = models.DateTimeField("Notification date")
    workorderid = models.ForeignKey(Workorder, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, related_name='roles')