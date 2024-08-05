import csv
from django.core.management.base import BaseCommand
from movies.models import Person, Movie, MoviePerson

class Command(BaseCommand):
    help = 'Import persons and movies data from TSV files...'

    def add_arguments(self, parser):
        parser.add_argument('persons_tsv', type=str, help='Path to the persons TSV file')
        parser.add_argument('movies_tsv', type=str, help='Path to the movies TSV file')

    def handle(self, *args, **kwargs):
        persons_tsv = kwargs['persons_tsv']
        movies_tsv = kwargs['movies_tsv']

        def convert_value(value):
            return None if value == "\\N" else value

        # Import movies
        with open(movies_tsv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                movie, created = Movie.objects.get_or_create(
                    nconst = row['tconst'],
                    defaults = {
                        'type': row['titleType'].strip(),
                        'title': row['primaryTitle'].strip(),
                        'orig_title': row['originalTitle'].strip(),
                        'is_adult': int(row['isAdult'].strip()),
                        'startYear': row['startYear'].strip(),
                        'endYear': row['endYear'].strip(),
                        'runtimeMinutes': int(convert_value(row['runtimeMinutes'])) if convert_value(row['runtimeMinutes']) else None,
                        'genres': row['genres'].strip(),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added movie {movie.title}'))

        # Import persons and movie-person relationships
        with open(persons_tsv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                person, created = Person.objects.get_or_create(
                    nconst = row['nconst'],
                    defaults = {
                        'full_name': row['primaryName'].strip(),
                        'birthYear': row['birthYear'].strip(),
                        'deathYear': row['deathYear'].strip(),
                        'profession': row['primaryProfession'].strip()
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added person {person.full_name}'))

                # Handle multiple comma-separated nconst values for movies
                movie_nconsts = row['knownForTitles'].strip().split(',')
                for movie_nconst in movie_nconsts:
                    try:
                        movie = Movie.objects.get(nconst=movie_nconst.strip())
                        MoviePerson.objects.get_or_create(
                            movie=movie,
                            person=person
                        )
                        self.stdout.write(self.style.SUCCESS(f'Linked {person.full_name} to movie {movie.title}'))
                    except Movie.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f'Movie with nconst {movie_nconst} does not exist'))
