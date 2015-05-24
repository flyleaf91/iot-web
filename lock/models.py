from django.db import models


class LockInfo(models.Model):
    device_id = models.CharField(max_length=128, db_index=True)
    event_type = models.IntegerField()
    event_time = models.DateTimeField(db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lock_info'


class LockCmd(models.Model):
    device_id = models.CharField(max_length=128, db_index=True)
    user = models.CharField(max_length=32, db_index=True, null=True)
    command = models.CharField(max_length=128)
    status = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lock_cmd'
