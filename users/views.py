from django.shortcuts import render
from rest_framework import generics

from .models import User

from .serializers import UserSerializer


import os
import zipfile
from django.http import HttpResponse
from django.conf import settings


def download_zip(request):

    folder_path = os.path.join(settings.MEDIA_ROOT, "files")

    # Name of the ZIP file
    zip_filename = "my_files.zip"

    # Create a response object with the appropriate ZIP headers
    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = f"attachment; filename={zip_filename}"

    # Create a ZIP file in memory
    with zipfile.ZipFile(response, "w") as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

    return response


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
