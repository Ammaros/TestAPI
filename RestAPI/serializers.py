from rest_framework import serializers
from .models import SignUpModel

class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SignUpModel
        fields = ('id', 'name', 'email', 'password')
    
    def save(self):
        account = SignUpModel(
            name = self.validated_data['name'],
            email = self.validated_data['email'],
            password = self.validated_data['password'],
        )

        account.save()
        return account