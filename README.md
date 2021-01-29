## Introduction

The idea to solve a problem that I had experienced since the beginning of times (to find a partner for pair programming with availability) was pushing me to spend some time on this personal project, deliver a functional product and then step by step make it better to reach its full potential.

Or in case it can serve a double purpose, I can make small increment commits which will allow people who are learning web development to see the progress and have a better understanding.

### STEPS

The first step would be to set up a virtual environment. More info here:
https://docs.python.org/3/tutorial/venv.html

`python3 -m venv local-env`

And then accessing that virtual environment in case we need to add a specific python package.

`source local-env/bin/activate`

The second step would be to create a .gitignore file that will allow us to avoid commiting and pushing content specified in this file to github (for instance the content inside our virtual environment).

As a note, we are going to use Flask to develop our web application. 

https://palletsprojects.com/p/flask/

The third step would be to start writing our app (inside app.py). Here you can name your file whatever you want, but for our purpose to keep things simple I am naming it app.py, which is the default needed when setting up the Procfile for Heruku, later on (do not worry about this now).

If you are familiar with Python, you already now that we can create Python packages to re-use code. In this case, since this could add complexity to a simple line of thought, in this initial version I am not considering writing a package for the app components.

Since we are ready to start writing the app in app.py, we will need to import the required packages for our app to work. But we cannot import something that we do not have installed yet. So, better to starts installing the packages with pip, the first one is Flask.

https://flask.palletsprojects.com/en/1.1.x/installation/

`pip3 install Flask`

When we install a package, that package might automatically install the packages that it requires, we can look into the documentation above, or check directly what was installed into our environment, for that we run:

`pip3 freeze > requirements.txt`

We can see that inside requirements.txt it indicates that Flask has been installed, we can proceed and import in our app.py file and no error will be thrown.

We then add the code for the minimal application with Flask.

At this point it might be good to run the application to see if it works fine.

There are several ways you can start your application, but since I am running on MacOS I will be using the one described below:

`FLASK_APP=app FLASK_ENV=development flask run`

After running the command above, a folder _ __pycache__ _ is created, since we do not need the content to be part of our repository, we add the folder into our .gitignore file.

To test that our application is fine, we could open any browser and go to the address: http://localhost:5000/, and we will see the message: Hello, World!

We can also use curl to see it it works right into our console (Might add details about this).

Here we have the endpoins I'm going to build:

###Endpoints

- GET '/users'
- GET '/users/<int:id>'
- POST '/users'
- PATCH '/users/<int:id>'
- DELETE '/users/<int:id>'

- GET '/appointments'
- GET '/appointments/<int:id>'
- POST '/appointments/'
- PATCH '/appointments/<int:id>'
- DELETE '/appointments/<int:id>'

For the moment, the app will be built with two models: user and appointment.

To control the SQLAlchemy integration with the app. We need to install Flask-SQLAlchemy. It will allow us to leverage all the functions and helpers from both sqlalchemy and sqlalchemy.orm 

`pip3 install Flask-SQLAlchemy`

And then run again 

`pip3 freeze > requirements.txt`

Deriving from the minimal installation [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application), lets start defining the models.

It is important to mention that here we have adopted the approach to wrap all the initial configuration to use a database with Flask-SQLAlchemy within a method:

```
def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()
  return db 
```

We have also defined methods to implement CRUD operations within the User class, which inherits from _db.Models_.

Here, we need to take a look into databases, not because the app needs us to know, just because it is always good to know what is happening under the hood.


### Creating a local PostgreSQL Database

If we user the shell, we create a database called pair-p like this:

`createdb pair-p`

To access the database, first we need to access psql by typing this:

`psql`

If we want to know all the databases in our local postgres we type:

`\l`

If you happen to name your database 'pair-p', to enter the database you use:

`\c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}`

In this case we only need to input this:

`\c pair-p Wilder`

Since at this point we have not yet stored data, the database is empty, so running the `\dt` command will show: _Did not find any relations._, in case we have data, it will list the tables in the database.


Since our application requires to interact with incoming data, we can use the class flask.Request.


From the [Flask webpage](https://flask.palletsprojects.com/en/1.1.x/api/#module-flask.json) you can read something like "jsonify adds a few enhancements to make life easier". So, we need to import jsonify:

`from flask import jsonify`

**Quick note**: The browser is from my point of view a huge Operating System, so it does a lot of things that we certainly do not know. Here, since our application is programmed to accept a json, the tests in postman have to specify that we are sending _Content Type: application/json_

To handle http exceptions gracefully we can make good use of an useful function abort

`from flask import abort`

### Database Migration

At this point, we have realized our original schema for our database needs some changes. The course of action would be to migrate the database and this can be accomplished by an extension that handles SQLAlchemy database migrations for Flask applications using Alembic: 

```
pip3 install Flask-Migrate
pip3 freeze > requirements.txt
```
Once we have our new models modified, we run (only the first time)

`flask db init`

Then,

```
flask db migrate -m "Added relationship between users and appointments"
flask db upgrade
```

**Note:** Running _flask db init_ throws an error because _No module named 'psycopg2'_

**Note:** On Mojave 10.14.6. there might be an issue installing psycopg2, [here](https://github.com/python-pillow/Pillow/issues/3438#issuecomment-435169249) is a very likely solution.

