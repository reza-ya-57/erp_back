from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes , api_view
from .models import CustomUser
from .serializers import CustomUserSerializer
# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_user(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users , many=True)
    response = Response(serializer.data)
    print(response)
    return response

