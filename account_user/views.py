from rest_framework import status
from requests import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import UserinfoSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def get_user_info(request):
    if request.user.is_authenticated:  # Check authentication for security
        # You can perform actions that require authentication here
        # ...

        if request.data:  # Check if data is provided in the request body
            serializer = UserinfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  # Save the new user object
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'error': 'No data provided in request body'})
    else:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
