FROM python:3.6-alpine

# Ensure packages are up to date and install some useful utilities
RUN apk update && apk add git vim postgresql-dev libffi-dev gcc musl-dev \
	libxml2-dev libxslt-dev

# From now on, work in the application directory
WORKDIR /usr/src/app

# Copy Docker configuration and install any requirements. We install
# requirements/docker.txt last to allow it to override any versions in
# requirements/requirements.txt.
ADD ./requirements/* ./requirements/
RUN pip install --no-cache-dir -r requirements/base.txt && \
	pip install --no-cache-dir -r requirements/docker.txt

# Copy the remaining files over
ADD . .

# Default environment for image.
#
# DANGER WILL ROBINSON! This file includes a baked-in secret key. This is
# because this application has NO web interface and therefore does not need to
# have cookie encryption, etc. Django still complains if SECRET_KEY is unset so
# we set it here.
#
# By default, we use the settings module bundled
# with this repo. Change DJANGO_SETTINGS_MODULE to install a custom settings.
#
# You probably want to modify the following environment variables:
#
# DJANGO_DB_ENGINE, DJANGO_DB_HOST, DJANGO_DB_PORT, DJANGO_DB_USER
ENV \
    DJANGO_SECRET_KEY=this-key-is-not-secret-in-any-meaningful-way-read-the-comment-above \
    DJANGO_SETTINGS_MODULE=gatherstats_project.settings.docker

ENTRYPOINT ["./manage.py"]
