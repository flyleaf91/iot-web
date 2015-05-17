from django.db import models


class User(models.Model):
    user = models.CharField(max_length=32, db_index=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'appuser'


class Login(models.Model):
    user = models.CharField(max_length=32, db_index=True)
    login_key = models.CharField(max_length=64)
    valid_end_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'login'
