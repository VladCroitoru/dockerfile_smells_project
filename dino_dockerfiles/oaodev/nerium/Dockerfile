FROM python:3.9.2-slim-buster
LABEL maintainer='Thomas Yager-Madden <thomas@yager-madden.com>'

# install git to support Nerium commit endpoint
RUN apt-get update && apt-get install -y git
# Copy in the code
COPY . /app

WORKDIR /app

# install from code currently in repo
RUN pip3 install -r requirements.txt

# install gunicorn and psycopg2 Postgres database driver
RUN pip3 install gevent gunicorn psycopg2-binary

VOLUME /app/query_files
VOLUME /app/format_files
EXPOSE 5000 

CMD gunicorn -c gunicorn_conf.py nerium.app:app
