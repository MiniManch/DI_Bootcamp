import flask
from app.films_bp import models, films_bp, forms
from app import db

@films_bp.route("/")
@films_bp.route("/homepage")
def index():
    films = models.Film.query.all()
    film_list = []
    for film in films:
        if len(film.director)>0:
            director = film.director[0]
        else:
            director = None
        film = {'film':film,'director':director}
        film_list.append(film)
    return flask.render_template("index.html", countries=models.Country, films=film_list)


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
    return flask.render_template("director/add.html", form=form, title='Add Director')


# create edit director route,form,template
@films_bp.route("/edit/director/<int:director_id>", methods=['GET', 'POST'])
def edit_director_func(director_id):
    form = forms.AddDirectorForm()
    director_to_edit = models.Director.query.filter_by(id=director_id).first()
    if director_to_edit is None:
        flask.flash('Director Does not exist')
        return flask.redirect(flask.url_for('films_bp.index'))
    if form.validate_on_submit():
        director_to_edit.first_name = form.first_name.data
        director_to_edit.last_name  = form.last_name.data
        db.session.commit()
        flask.flash(f'Director was edited successfully!')
        return flask.redirect(flask.url_for('films_bp.index'))
    return flask.render_template('director/edit.html', form=form, director=director_to_edit, title='Edit Director')


# create edit film route, form, template
@films_bp.route("/edit/film/<int:film_id>", methods=['GET', 'POST'])
def edit_film_func(film_id):
    form = forms.AddFilmForm()
    film_to_edit = models.Film.query.filter_by(id=film_id).first()
    if film_to_edit is None:
        flask.flash('Film Does not exist')
        return flask.redirect(flask.url_for('films_bp.index'))
    if form.validate_on_submit():
        film_to_edit.release_date = form.release_Date.data
        film_to_edit.title  = form.title.data
        country = models.Country.query.filter_by(name=form.country_created_in.data).first()
        if country is None:
            country =models.Country(name=form.country_created_in.data)
            db.session.add(country)
            db.session.commit()
        film_to_edit.created_in_country =  country.id
        film_to_edit.categories[0].name     = form.category.data
        db.session.commit()
        flask.flash(f'Film was edited successfully!')
        return flask.redirect(flask.url_for('films_bp.index'))
    country = models.Country.query.filter_by(id=film_to_edit.created_in_country).first().name
    return flask.render_template('film/edit.html', form=form, film=film_to_edit, country=country, title='Edit Film')
