from rest_framework import viewsets
from account_management.models import MediaLibrary
from account_management.serializers.media_library_serializers import MediaLibrarySerializer


class MediaLibraryViewSet(viewsets.ModelViewSet):
    queryset = MediaLibrary.objects.all()
    serializer_class = MediaLibrarySerializer


