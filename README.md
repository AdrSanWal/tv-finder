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

2. Build and run docker

      Go to folder/tv-finder and run:
      
      docker-compose up -d --build

3. Get the CONTAINER ID

      In the same folder run:
      
      docker ps
      
      Identify the CONTAINER ID of the tv-finder_django image
  
4. Start a session within the default directory of the container

      In the same folder run:
      
      docker exec -it CONTAINER ID bash
      
5. Fill database with some examples

      Go to code/tvfinder and run:
      
      python3 fill_database.py    
  
5. Use the app
      
      Go to localhost:8000/f to use it
