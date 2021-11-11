
FROM ubuntu:14.04

MAINTAINER Anton Golubtsov <agolubts@yandex.ru>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install \
               cmake \
               gcc \
               git \
               libyaml-cpp-dev \
               nginx \
               python-dev \
               python-pip \
               sed \
               ssh \
               supervisor \
               uwsgi-plugin-python \
               vim \
               wget

WORKDIR /tmp
RUN wget -q https://github.com/libgit2/libgit2/archive/v0.20.0.tar.gz
RUN tar xzf v0.20.0.tar.gz
WORKDIR libgit2-0.20.0
RUN cmake . -DCMAKE_INSTALL_PREFIX=/usr && make && make install

WORKDIR /
RUN rm -rf /tmp/*

RUN mkdir -p /var/log/nginx/app
RUN mkdir -p /var/log/uwsgi/app/

RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
COPY uwsgi.ini /var/www/app/


RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY app /var/www/app
COPY requirements.txt /var/www/app/
RUN pip install -r /var/www/app/requirements.txt

EXPOSE 80 443

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
