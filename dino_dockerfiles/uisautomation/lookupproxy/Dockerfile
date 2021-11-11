FROM python:3.6

WORKDIR /usr/src/app

ADD ./requirements*.txt /usr/src/app/
RUN pip install -r ./requirements_docker.txt

ADD ./ /usr/src/app/

ENV DJANGO_SETTINGS_MODULE=lookupproxy.settings.docker
ENTRYPOINT ["scripts/docker-entrypoint.sh"]
