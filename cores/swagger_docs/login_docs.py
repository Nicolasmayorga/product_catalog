
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from cores.views import login  # Importando la función vista 'login'

description = """
Log in by providing the username and password.

If the credentials are valid, the response will contain refresh and access tokens.
"""

login = swagger_auto_schema(
    method='post',
    operation_description=description,
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
        },
    ),
    responses={
        200: openapi.Response(description='Authentication successful', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh Token'),
                'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access Token')
            }
        )),
        401: "Invalid credentials"
    }
)(login)
