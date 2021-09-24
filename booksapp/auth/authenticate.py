import jwt
from rest_framework import authentication
from django.conf import settings

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        
        return super().authenticate(request)