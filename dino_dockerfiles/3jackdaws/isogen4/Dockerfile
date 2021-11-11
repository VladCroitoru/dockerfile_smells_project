FROM 	python:latest

RUN 	pip3 install django pymysql pillow gunicorn misaka pygments xmltodict mutagen redis

WORKDIR /var/www
RUN mkdir isogen
COPY . isogen/

VOLUME /var/www/isogen

WORKDIR /var/www/isogen


CMD ["gunicorn", "-b", "0.0.0.0:80","isogen4.wsgi"]
