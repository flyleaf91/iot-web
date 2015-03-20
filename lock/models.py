from django.db import models

# Create your models here.
class LockInfo(models.Model):
    device_id = models.CharField(max_length=128, db_index=True)
    event_type = models.IntegerField()
    event_time = models.DateTimeField(db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lock_info'