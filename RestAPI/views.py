from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import SignUpSerializer
from .models import SignUpModel

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUpModel.objects.all().order_by('id')
    serializer_class = SignUpSerializer

    @api_view(['POST'])
    def create_auth(request):
        serialized = SignUpSerializer(data=request.DATA)
        if serialized.is_valid():
            user = serialized.save()
            if user:
                token = Token.objects.create(user=user)
                json = serialized.data
                json['token'] = token.key
                return Response(json)
        else:
            return Response(serialized._errors)
