from rest_framework import viewsets
from apps.user.models import User
from apps.user.serializer import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['password', 'username']
	permission_classes = [AllowAny]

	def perfom_create(self, serializer):
		new_user = User.objects.create(username=self.request.data.get("username"))
		new_user.set_password(self.request.data.get("password"))
		serializer.save(password=user.password)