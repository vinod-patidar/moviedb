# moviedb API

## Table of Contents

- [Project Layout](#project-layout)
- [Setting up the moviedb api project](#setting-up-the-moviedb-project)
- [Setting up the moviedb project manually](#setting-up-the-moviedb-project-manually)

---

## Project Layout
  
  Here is the project layout and Architecture:
  
  ```
  moviedb
   |__ movies/
      |__ urls.py
      |__ serializers.py
      |__ views
      |__ tests
   |__ moviedb/
      |__ __init__.py/
      |__ .env
      |__ asgi.py
      |__ settings.py
      |__ urls.py
      |__ wsgi.py
   |__ .gitignore
   |__ manage.py
   |__ requirements.txt
   |__ README.md
  
  ```
  
  ## Setting up the `moviedb` project
  
  Start by cloning the project with the command:
  ```
  $ git clone https://github.com/vinod-patidar/moviedb.git
  ```
 
  ## Setting up the `moviedb` project manually
  
  - setup the moviedb project manually follow the directions below.
  - Go to the project root and start by installing the dependencies for the api:
  - Create virtual enviorment
  ```
  $ cd moviedb/
  $ python -m venv env
  ```
  
  Let's activate the virtual enviorment first.
  - To run the below command and run in terminal from root directory:
  ```
  $ source env/bin/activate
  ```

  - Installing the dependencies for the api:
  ```
  $ cd moviedb/
  $ pip install -r requirements.txt
  ```

  Let's run few python management commands to db setup.
  - To run the below command and run in terminal from root directory:
  ```
  $ cd moviedb/moviedb
  
  $ python manage.py makemigrations
  $ pyhton manage.py migrate
  ```

  Let's run this command to import movies DB files.
  - To run the below command and run in terminal from root directory:
  ```
  $ python manage.py import_data ./uploads/name.basics.tsv ./uploads/title.basics.tsv
  ```

  Let's start the api backend server.
  - To run the below command and run in terminal from root directory:
  ```
  $ python manage.py runserver
  ```

  - Now, go to http://localhost:8000/ in your browser.
  - Ready to use :)

