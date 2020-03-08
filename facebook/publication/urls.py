#publication URLSs
#Django
from django.urls import include, path
from rest_framework.routers import DefaultRouter
#views
from .views import publication as publication_views

router = DefaultRouter()
router.register(r'publication', publication_views.PublicationViewSet, basename='publication')
urlpatterns = [
    path('', include(router.urls))
]