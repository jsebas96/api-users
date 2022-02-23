from .models import User
from .serializers import UserSerializer
from rest_framework import response, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.
class CreateUserView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        username = request.query_params.get('username', None)

        if username != None:
            user = get_object_or_404(User, username = username)
            serializer = UserSerializer(user)
            return response.Response(serializer.data, status.HTTP_200_OK)
        return response.Response(None, status.HTTP_400_BAD_REQUEST)