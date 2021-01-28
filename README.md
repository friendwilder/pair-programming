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

The third step would be to start writing our app (inside app.py). Here you can name your file whatever you want, but for our purpose to keep things simple I am naming it app.py, which is the default needed when setting up the Procfile for Heruku, later on (do not worry about this now).

If you are familiar with Python, you already now that we can create Python packages to re-use code. In this case, since this could add complexity to a simple line of thought, in this initial version I am not considering writing a package for the app components.

