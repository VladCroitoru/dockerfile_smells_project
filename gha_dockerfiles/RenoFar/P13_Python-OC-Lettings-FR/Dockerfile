# base image
FROM python:3.9
# setup environment variable
ENV DockerHOME=/app

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG='development'
ENV PORT=8000

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME

# run this command to install all dependencies
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# Collect all static files in app.
# Already done for having the same version of the app on every environnement
#RUN python manage.py collectstatic --noinput --clear

# start server
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT