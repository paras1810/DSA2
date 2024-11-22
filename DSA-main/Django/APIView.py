from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelAPIView(APIView):
    """
    A view that returns a list of YourModel.
    """
    def get(self, request, format=None):
        """
        Return a list of all YourModel objects.
        """
        queryset = YourModel.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new YourModel object.
        """
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
