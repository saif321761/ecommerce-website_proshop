from rest_framework import serializers  # Fix typo here
from django.contrib.auth.models import User
from .models import Product
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User  # Fix typo here
        fields = ['id','_id','username','email','name','isAdmin']

    def get__id(self, obj):
        return obj.id
    
    def get_isAdmin(self,obj):
        return obj.is_staff

    def get_name(self,obj): # object is going to be the user object
        name = obj.first_name
        if name == '':
            name = obj.email
        return name
class ProductSerializer(serializers.ModelSerializer):  # Fix typos here
    class Meta:
        model = Product  # Fix typo here
        fields = '__all__'
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = fields = ['id','_id','username','email','name','isAdmin', 'token']
    def get_token(self, obj):

        token = RefreshToken.for_user(obj)
        return str(token)