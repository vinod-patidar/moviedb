from rest_framework import serializers
from .models import Movie, Person, MoviePerson

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = '__all__'

class MoviePersonSerializer(serializers.ModelSerializer):
  person = PersonSerializer()

  class Meta:
    model = MoviePerson
    fields = ['person', 'role']

class MovieSerializer(serializers.ModelSerializer):
  persons = MoviePersonSerializer(source='movieperson_set', many=True, read_only=True)

  class Meta:
    model = Movie
    fields = '__all__'


# from rest_framework import serializers
# from movies.models import Movie, Person

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ['nconst', 'first_name', 'last_name']

# class MovieSerializer(serializers.ModelSerializer):
#     associated_persons = PersonSerializer(many=True, source='person_set')  # Adjust the related field name if needed

#     class Meta:
#         model = Movie
#         fields = ['title', 'year', 'runtime_minutes', 'associated_persons']
    
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['endYear'] = instance.year
#         representation['type'] = 'Movie'
#         representation['genres'] = []
#         return representation
