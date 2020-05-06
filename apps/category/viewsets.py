from rest_framework import viewsets
from apps.category.models import Category
from apps.category.serializer import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['presupuesto','usuario']