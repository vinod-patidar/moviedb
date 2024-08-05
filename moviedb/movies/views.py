from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Person, MoviePerson
from .serializers import MovieSerializer, PersonSerializer, MoviePersonSerializer


class MovieViewSet(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer


class PersonViewSet(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound
# from movies.models import Movie
# from .serializers import MovieSerializer

# class MovieSearchView(generics.GenericAPIView):
#     serializer_class = MovieSerializer

#     def get(self, request, *args, **kwargs):
#         title = request.query_params.get('title', None)
#         if not title:
#             return Response({'error': 'Title parameter is required'}, status=400)

#         movies = Movie.objects.filter(title__icontains=title)
#         if not movies.exists():
#             raise NotFound(detail='No movies found with the given title')

#         serializer = self.get_serializer(movies, many=True)
#         return Response(serializer.data)

