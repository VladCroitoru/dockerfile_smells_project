# https://testdriven.io/blog/deploying-django-to-heroku-with-docker/
# https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

# pull official base image
FROM python:3.8-alpine

# add maintainer / contact details to container in form of key=value metadata
LABEL maintainer_name="Sven Gerlach" \
      maintainer_email="svengerlach@me.com"

# set work directory
# Github Actions recommends not to set WORKDIR
# https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions#workdir
# not clear at all how else to set the working directory
WORKDIR /app

# install psycopg2 (needs to be installed manually rather than through executing the Pipfile
RUN apk update && apk add \
    gcc \
    libc-dev \
    python3-dev \
    musl-dev \
    postgresql-dev \
    vim \
    # install bash (alpine ships with ash)
    # access bash with "docker exec -it <container-name> /bin/bash"
    bash --no-cache --upgrade

# source: https://jonathanmeier.io/using-pipenv-with-docker/
# install pipenv and install dependencies
RUN pip install \
    pipenv \
    psycopg2
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --pre

# copy project
COPY . .

# collectsttic has to be run during build-time. If it is run at run-time static files will not
# persist on Heroku. However, at build-time settings.py doesn't have access to the django secret
# key stored as an env on heroku. To get around this issue the settings.py file uses a default
# secret key as a fall-back option.
# https://stackoverflow.com/questions/59719175/where-to-run-collectstatic-when-deploying-django-app-to-heroku-using-docker
RUN python manage.py collectstatic --noinput

# Heroku strongly recommends running the container as a non-root user as that is exactly how
# Heroku wil run the created container for deployment
# However, setting a non-root user prevents access to GITHUB_WORKSPACE
# https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions#user
#RUN adduser -D generic_user
#USER generic_user

# run gunicorn
CMD gunicorn secure_my_spot.wsgi:application --bind 0.0.0.0:$PORT
