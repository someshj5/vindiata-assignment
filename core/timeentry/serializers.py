from rest_framework import serializers
from rest_framework.decorators import action
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task

    @action(methods=['put'], detail=False)
    def update(self, instance, validated_data):
        print(validated_data, 'validated_data')
        instance.name = validated_data.get('name', instance.name)
        instance.project = validated_data.get('project', instance.project)
        instance.start_time = validated_data.get(
            'start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.start = validated_data.get('start', instance.start)
        instance.finish = validated_data.get('finish', instance.finish)
        # instance.created_by = validated_data.get(
        #     'created_by', instance.created_by),
        instance.save()
        return instance

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {'created_by': {'read_only': True}}
