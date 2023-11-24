from rest_framework import routers # Importa el módulo routers de Django Rest Framework, que proporciona una forma sencilla de definir rutas URL para las vistas.
from .api import * # Importamos todas las vistas que definimos en el archivo api.py

router = routers.DefaultRouter() # Crea una nueva instancia de DefaultRouter, que es una clase de enrutador que automáticamente crea rutas URL para las vistas, basándose en los métodos que definen.
router.register('api/categories', CategoryViewSet, 'categories') # Registra la vista CategoryViewSet con el enrutador bajo la ruta URL api/categories. El tercer argumento, 'categories', es un nombre opcional que se puede usar para referirse a esta ruta URL en otras partes del código.
router.register('api/books', BookViewSet, 'books')
urlpatterns = router.urls # Asigna las rutas URL generadas por el enrutador a urlpatterns, que es la variable que Django utiliza para determinar las turas URL de la aplicación