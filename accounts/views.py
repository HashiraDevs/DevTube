from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from allauth.socialaccount.providers.oauth2.client import OAuth2C
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapterlient
from dj_rest_auth.registration.views import SocialLoginView


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



class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/"
    client_class = OAuth2Client
