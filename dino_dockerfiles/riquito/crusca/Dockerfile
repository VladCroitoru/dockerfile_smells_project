FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# pyvenv (or virtualenv) is not needed since it's a docker image
# but I find more educational to use it anyway.
RUN pyvenv /env

# add just requirements.txt for now for better caching
ADD requirements.txt /usr/src/app
RUN /env/bin/pip3 install --no-cache-dir uwsgi && \
    /env/bin/pip3 install -r requirements.txt

ADD . /usr/src/app
VOLUME /usr/src/app/config/config.yml

ENV ENVIRONMENT DEVELOPMENT

EXPOSE 3031
EXPOSE 9091

ENTRYPOINT /env/bin/uwsgi --ini uwsgi.ini

