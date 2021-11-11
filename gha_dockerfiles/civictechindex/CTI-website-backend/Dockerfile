FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
# Disable writing .pyc files - but only during docker build
ARG PYTHONDONTWRITEBYTECODE=1

RUN apt-get update -y \
 && apt-get install -y gnupg2 wget \
 && wget --quiet -O /tmp/pg-repo.asc https://www.postgresql.org/media/keys/ACCC4CF8.asc \
 && apt-key add /tmp/pg-repo.asc \
 && echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" >  /etc/apt/sources.list.d/pgdg.list \
 && apt-get update -y \
 && apt-get install -y libenchant-dev libpq-dev postgresql-client-12 \
 # dependencies for building Python packages
 && apt-get install -y build-essential procps \
 # Translations dependencies
 && apt-get install -y gettext \
 # cleaning up unused files
 && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
 && rm -rf /var/lib/apt/lists/*

# create root directory for our project in the container
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /code/
RUN /code/manage.py collectstatic --no-input -v0 -i node_modules --link

EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
