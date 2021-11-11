FROM python:slim

RUN apt-get update
RUN apt-get -y install nginx supervisor git
RUN pip install --no-cache-dir gunicorn Flask

RUN apt-get install -y python-pip
RUN apt-get install -y mongodb-clients
RUN pip install pymongo
RUN apt-get install -y curl
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app

# nginx setup
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# supervisor setup
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/
COPY gunicorn.conf /etc/supervisor/conf.d/

EXPOSE 80
CMD ["/usr/bin/supervisord"]
