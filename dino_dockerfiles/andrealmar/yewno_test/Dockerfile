FROM ubuntu:14.04
MAINTAINER Andre Araujo <andre@y7mail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y curl nginx sed python-pip python-dev gunicorn supervisor vim

FROM python:3.5
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

# Setup Flask app
# RUN mkdir -p /deploy/app
# COPY app /deploy/app
# RUN pip install -r /deploy/app/requirements.txt

# Setup nginx
# RUN rm /etc/nginx/sites-enabled/default
# COPY flask.conf /etc/nginx/sites-available/
# RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf

#Setup Supervisor
# RUN mkdir -p /var/log/supervisor
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Start processes
# CMD ["/usr/bin/supervisord"]
