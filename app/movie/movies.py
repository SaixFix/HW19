from flask_restx import Namespace, Resource

from app.dao.models import Movie, MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Получаем список всех фильмов"""
        movies = Movie.query.all()
        return movies_schema.dump(movies), 200

    def post(self):
        """Добовление фильма"""
        return "", 201


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        """Получаем фильм по id"""
        try:
            movie = Movie.query.filter(Movie.id == id).one()
            return movie_schema.dump(movie), 200
        except Exception as error:
            return str(error), 404

    def put(self, id):
        """Обновление фильма по id"""
        return "", 200

    def delete(self, id):
        """Удаление по id"""
