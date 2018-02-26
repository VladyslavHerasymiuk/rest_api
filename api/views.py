from rest_framework import generics
from .serializers import Users_Serializer
from .models import Users

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Users.objects.all()
    serializer_class = Users_Serializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Users.objects.all()
    serializer_class = Users_Serializer