from apps.user.models import User
from rest_framework import serializers, fields
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
	class Meta: 
		model = User
		fields = ('id','password','username','first_name','last_name','email')
	def create(self, validate_data):
		validate_data['password'] = make_password(validate_data['password'])
		return super(UserSerializer, self).create(validate_data)