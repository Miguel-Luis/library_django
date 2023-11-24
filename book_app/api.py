from rest_framework import viewsets, permissions # Se importa los módulos, viewsets y permissions de Django Rest Framework
from .models import * # Se importa los modelos de la aplicación book_app del archivo models.py
from .serializers import * # Importa los serializadores que definimos en serializers.py

'''
La clase CategoryViewSet hereda de viewsets.ModelViewSet,
lo que significa que proporciona operaciones CRUD
completas para el modelo Category
'''
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # Se define el conjunto de datos que esta vista manejará
    permission_classes = [permissions.AllowAny] # Esto establece las clases de permisos para la vista. En este caso, AllowAny significa que cualquier usuario, autenticado o no, puede acceder a esta vista.
    serializer_class = CategorySerializer # Establece la clase de serializador para la vista. El serializador define cómo se convierten los objetos de modelo Category en JSON para ser enviados a través de la API.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer