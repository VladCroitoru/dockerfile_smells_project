# A container which runs nginx, uwsgi and flask.
# flask app will be in /data
# If you want to use your own nginx, uwsgi configuration,
# replace them with your own by
# COPY my-nginx.conf /etc/nginx/


FROM ubuntu:14.04

maintainer gensmusic <gensmusic@163.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:nginx/stable && \
    apt-get update && \
    apt-get install -y build-essential git python python-dev python-setuptools \
            nginx supervisor libmysqlclient-dev \
            libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install uwsgi and cleanup the cache
RUN easy_install pip && \
    pip install uwsgi --cache-dir=/tmp/pip_cache && \
    rm -rf /tmp/pip_cache

RUN mkdir -p /var/log/uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/
COPY supervisor.conf /etc/supervisor/conf.d/
RUN mkdir -p /etc/uwsgi/vassals
COPY uwsgi.ini /etc/uwsgi/vassals/

EXPOSE 80 443

CMD ["supervisord", "-n"]

# COPY run.sh /usr/local/bin/run.sh
# CMD ["run.sh"]