import flask
from app.films_bp import models, films_bp, forms
from app import db


@films_bp.route("/homepage")
def index():
    return flask.render_template("index.html", countries=models.Country, films=models.Film.query.all())


@films_bp.route("/addFilm", methods=['GET', 'POST'])
def add_film_func():
    form = forms.AddFilmForm()
    if form.validate_on_submit():
        #check if title not in all the films
        if models.Film.query.filter_by(title=form.title.data).first() is not None:
            flask.flash(f'this film already exists in our database!')
            return flask.redirect(flask.url_for('films_bp.add_film_func'))

        #define the country, define the director
        if  models.Country.query.filter_by(name=form.country_created_in.data).first() is not None:
            country_in = models.Country.query.filter_by(name=form.country_created_in.data).first()
        else:
            country_in = models.Country(name=form.country_created_in.data)
            db.session.add(country_in)
            db.session.commit()

        new_film = models.Film(title=form.title.data,
                               release_date=form.release_Date.data,
                               created_in_country=country_in.id,
                               categories=[],
                               director=[],
                               available_in_countries=[])

        if models.Category.query.filter_by(name=form.category.data).first() is None:
            category = models.Category(name=form.category.data.lower().capitalize())
        else:
            category = models.Category.query.filter_by(name=form.category.data).first()

        new_film.categories.append(category)
        db.session.add(new_film)
        db.session.commit()

        flask.flash(f'New film {form.title.data} was added successfully!')
        return flask.redirect(flask.url_for('films_bp.index'))
    return flask.render_template("film/add.html", form=form)


@films_bp.route("/addDirector", methods=['GET', 'POST'])
def add_director_func():
    form = forms.AddDirectorForm()
    if form.validate_on_submit():
        film  = models.Film.query.filter_by(title=form.film.data).first()
        directors = models.Director.query.filter_by(first_name=form.first_name.data)
        if directors.first() is not None:
            for director in directors:
                if director.last_name == form.last_name.data:
                    flask.flask(f'Director {film.first_name} {film.last_name} already exists!')
                    return flask.redirect(flask.url_for('films_bp.add_director_func'))
        if film is None:
            flask.flash(f'Film does not exist!')
            return flask.redirect(flask.url_for('films_bp.add_director_func'))

        director = models.Director(first_name=form.first_name.data,
                                   last_name=form.last_name.data,
                                   )
        db.session.add(director)
        film.director.append(director)
        db.session.commit()

        flask.flash(f'Director was added successfully!')
        return flask.redirect(flask.url_for('films_bp.index'))
    return flask.render_template("director/add.html", form=form)
