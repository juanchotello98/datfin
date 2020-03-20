from rest_framework import viewsets
from apps.category.models import Category
from .serializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer