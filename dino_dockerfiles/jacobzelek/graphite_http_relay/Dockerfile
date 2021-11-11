FROM python:2.7.11

MAINTAINER Jacob Zelek <jacob.zelek@gmail.com>

ADD config.json .
ADD main.py .
ADD nginx.conf .
ADD requirements.txt .
ADD supervisor.conf .
ADD uwsgi.ini .
ADD uwsgi_params .

WORKDIR /

RUN apt-get update
RUN apt-get install -y nginx supervisor
RUN pip install uwsgi
RUN pip install -r requirements.txt

RUN \
  echo "daemon off;" >> /etc/nginx/nginx.conf \
  && rm /etc/nginx/sites-enabled/default \
  && ln -s /nginx.conf /etc/nginx/sites-enabled/ \
  && ln -s /supervisor.conf /etc/supervisor/conf.d/

EXPOSE 80
CMD ["supervisord", "-n"]