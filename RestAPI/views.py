from rest_framework import viewsets
from .serializers import SignUpSerializer
from .models import SignUpModel

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUpModel.objects.all().order_by('id')
    serializer_class = SignUpSerializer

    # @api_view(['POST'])
    # def create_auth(request):
    #     serialized = SignUpSerializer(data=request.DATA)
    #     if serialized.is_valid():
    #         User.objects.create_user(
    #             serialized.init_data['email'],
    #             serialized.init_data['name'],
    #             serialized.init_data['password']
    #         )
    #         return Response(serialized.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
