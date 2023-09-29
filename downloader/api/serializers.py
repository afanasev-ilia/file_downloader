from rest_framework import serializers
from django.core.files.base import ContentFile

from files.models import File


class MyFileField(serializers.FileField):
    def to_internal_value(self, data):
        file_path = 'media/files/' + data.name
        with open(file_path, 'wb+') as temp_file:
            for chunk in data.chunks():
                temp_file.write(chunk)
        with open(file_path, 'rb') as temp_file:
            return super().to_internal_value(ContentFile(temp_file.read(), name=temp_file.name))


class FileSerializer(serializers.ModelSerializer):
    file = MyFileField()

    class Meta:
        model = File
        fields = ('file',)
