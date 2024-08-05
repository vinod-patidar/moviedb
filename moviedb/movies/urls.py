from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, PersonViewSet #, MovieSearchView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
  path('', include(router.urls)),
  # path('search-movie/', MovieSearchView.as_view(), name='search-movie'),
]
