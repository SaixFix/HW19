from app.dao.director_dao import DirectorDAO
from app.dao.movie_dao import MovieDAO
from app.services.director import DirectorService
from app.services.movie import MovieService
from app.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
