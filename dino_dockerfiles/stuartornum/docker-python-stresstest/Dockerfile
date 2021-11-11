FROM python:2-slim

RUN apt-get update && apt-get install nginx -y && apt-get clean all

ADD ./requirements.txt /requirements.txt
RUN /usr/local/bin/pip install -r /requirements.txt

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD . /srv

EXPOSE 8080
WORKDIR /srv
ENTRYPOINT ["/srv/run.sh"]

