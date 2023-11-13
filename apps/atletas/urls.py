from django.urls import path
from .views import atletas

urlpatterns = [
    path('blog/', atletas, name="pagina_blog")
    ]