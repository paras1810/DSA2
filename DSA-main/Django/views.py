from rest_framework.response import Response
from rest_framework.view import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, throttle_classes, schema
from rest_framework.throttling import UserRateThrottle
from rest_frameowrk.schemas import AutoSchema

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        pass


class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthrntication]
    permissions_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    
    @api_view
    def hello_world(request):
        return Response({"message": "Hello World"})
    
    @api_view(['GET', 'POST'])
    def hello_world2(request):
        if request.method == "POST":
            return Response({"message": "Hello WOrld2", "data": request.data})
        return Response({"message": "Hello World"})

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])    
@schema(CustomAutoSchema)
def view(request):
    return Response({"message": "Use of Throttle"})