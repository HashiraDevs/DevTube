from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    # Set the queryset to include all User objects
    queryset = User.objects.all()
    
    # Specify the serializer class to use for User registration
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Get an instance of the serializer with the data from the request
        serializer = self.get_serializer(data=request.data)
        
        # Validate the serializer data; raise an exception if validation fails
        serializer.is_valid(raise_exception=True)
        
        # Create a new User based on the validated serializer data
        self.perform_create(serializer)
        
        # Get the success headers for the HTTP response
        headers = self.get_success_headers(serializer.data)
        
        # Return a JSON response with the serialized User data and a status code of 201 Created
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)