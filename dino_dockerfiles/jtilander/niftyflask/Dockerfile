FROM phusion/baseimage:0.9.19
MAINTAINER Jim Tilander <jim@tilander.org>
CMD ["/sbin/my_init"]

# Ensure that the apt tool doesn't require any user interaction
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -qy --no-install-recommends nginx && \
    apt-get install -qy --no-install-recommends \
    python-software-properties \
    python-setuptools \
    build-essential \
    python-dev \
    python \
    git \
    vim \
    curl \
    less \
    wget \
    gettext-base \
    dos2unix && \
    apt-get install -qy postgresql postgresql-contrib && \
    apt-get install -qy --no-install-recommends \
	zlib1g-dev \
	libpng12-dev \
	libpq-dev \
	libldap2-dev \
	libsasl2-dev \
	libssl-dev \
	libjpeg-dev \
	libffi-dev \
	npm \
	nodejs \
	nodejs-legacy && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN easy_install pip
RUN pip install \
	uwsgi \
	flask \
	psycopg2 \
	alembic

EXPOSE 80

RUN mkdir -p /etc/my_init.d
ADD etc/init-nginx.sh /etc/my_init.d/nginx.sh

RUN mkdir -p /etc/service/nginx
ADD etc/run-nginx.sh /etc/service/nginx/run
RUN chmod a+x /etc/service/nginx/run

ADD etc/init-app.sh /etc/my_init.d/app.sh

RUN mkdir -p /etc/service/app
ADD etc/run-app.sh /etc/service/app/run
RUN chmod a+x /etc/service/app/run

RUN chmod a+x /etc/my_init.d/*.sh

ADD etc/nginx.conf /etc/nginx/nginx.template

RUN mkdir -p /app
RUN mkdir -p /etc/app
ADD etc/requirements.txt /etc/app
RUN pip install --upgrade -r /etc/app/requirements.txt

ADD etc/uwsgi.ini /etc/app/uwsgi.template

# Now that we have docker for windows as well, we need to fix the line endings
# potentially on the source code that we just added.
RUN dos2unix /etc/app/*.template
RUN dos2unix /etc/my_init.d/*.sh
RUN dos2unix /etc/service/nginx/run
RUN dos2unix /etc/service/app/run


RUN touch /app/mount_this_from_another_container

VOLUME /app
WORKDIR /app


ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=nifty
ENV UWSGI_HOTLOAD=0
ENV UWSGI_WORKERS=8
ENV NGINX_WORKERS=8
ENV PGHOST=postgres
