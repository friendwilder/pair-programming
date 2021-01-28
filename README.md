Introduction

The idea to solve a problem that I had experienced since the beginning of times was pushing me to spend some time on this personal project, deliver a functional product and then step by step make it better to reach its full potential.

Or in case it can serve a double purpose, I can make small increment commits which will allow people who are learning web development to see the progress and have a better understanding.

STEPS

The first step would be to set up a virtual environment. More info here:
https://docs.python.org/3/tutorial/venv.html

python3 -m venv local-env

And then accessing that virtual environment in case we need to add a specific python package.

source local-env/bin/activate

The second step would be to create a .gitignore file that will allow us to avoid commiting and pushing content specified in this file to github (for instance the content inside our virtual environment).

As a note, we are going to use Flask to develop our web application. 

https://palletsprojects.com/p/flask/

The third step would be to start writing our app (inside app.py). Here you can name your file whatever you want, but for our purpose to keep things simple I am naming it app.py, which is the default needed when setting up the Procfile for Heruku, later on (do not worry about this now).

If you are familiar with Python, you already now that we can create Python packages to re-use code. In this case, since this could add complexity to a simple line of thought, in this initial version I am not considering writing a package for the app components.

Since we are ready to start writing the app in app.py, we will need to import the required packages for our app to work. But we cannot import something that we do not have installed yet. So, better to starts installing the packages with pip, the first one is Flask.

https://flask.palletsprojects.com/en/1.1.x/installation/

pip3 install Flask

When we install a package, that package might automatically install the packages that it requires, we can look into the documentation above, or check directly what was installed into our environment, for that we run:

pip3 freeze > requirements.txt

We can see that inside requirements.txt it indicates that Flask has been installed, we can proceed and import in our app.py file and no error will be thrown.

We then add the code for the minimal application with Flask.

At this point it might be good to run the application to see if it works fine.

There are several ways you can start your application, but since I am running on MacOS I will be using the one described below:

FLASK_APP=app FLASK_ENV=development flask run

After running the command above, a folder __pycache__ is created, since we do not need the content to be part of our repository, we add the folder into our .gitignore file.

To test that our application is fine, we could open any browser and go to the address: http://localhost:5000/, and we will see the message: Hello, World!

We can also use curl to see it it works right into our console (Might add details about this)



