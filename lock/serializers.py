from rest_framework import serializers
import lock.models as models


class LockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LockInfo