Tv-finder
=
A project to search for movies and series and practice django


Parts of the project
=
* Scripts to fill the sqlite3 database with web scraping (fill_db)
* Django project (tvfinder)

Run project
=
1. Clone the repository in any folder

      git clone https://github.com/AdrSanWal/tv-finder.git

2. Install requirements

      go to folder/tv-finder and run:
      pip3 install -r requirements.txt

3. Migrate tables

      go to folder/tv-finder/tvfinder and run:
      python3 manage.py migrate
  
4. Create superuser

      In the same folder run:
      python3 manage.py createsuperuser
      you will need name, mail and password
  
5. Launch server

      In the same folder run:
      python3 manage.py runserver
  
While fill_db is not working (it is in process),
you can fill the database from http://localhost:8000/admin


