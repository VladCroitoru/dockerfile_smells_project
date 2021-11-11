FROM python:3.4
MAINTAINER Evan Rittenhouse <emanguy1@gmail.com>

# Install nginx
ENV NGINX_VERSION 1.9.7-1~jessie

RUN apt-key adv \
	  --keyserver hkp://pgp.mit.edu:80 \
	  --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        locales \
        ca-certificates \
        nginx=${NGINX_VERSION} \
    && rm -rf /var/lib/apt/lists/* \
	&& locale-gen en_US.UTF-8 && dpkg-reconfigure locales

COPY taiga-back /usr/src/taiga-back
COPY taiga-front-dist/ /usr/src/taiga-front-dist
COPY docker-settings.py /usr/src/taiga-back/settings/docker.py
COPY conf/locale.gen /etc/locale.gen
COPY conf/nginx/* /etc/nginx/

# Setup symbolic links for configuration files
RUN mkdir -p /taiga
COPY conf/taiga/* /taiga/
RUN ln -s /taiga/local.py /usr/src/taiga-back/settings/local.py \
	&& ln -s /taiga/conf.json /usr/src/taiga-front-dist/dist/js/conf.json

WORKDIR /usr/src/taiga-back

RUN pip install --no-cache-dir -r requirements.txt \
	&& echo "LANG=en_US.UTF-8" > /etc/default/locale \
	&& echo "LC_TYPE=en_US.UTF-8" > /etc/default/locale \
	&& echo "LC_MESSAGES=POSIX" >> /etc/default/locale \
	&& echo "LANGUAGE=en" >> /etc/default/locale

ENV LANG=en_US.UTF-8 \
	LC_TYPE=en_US.UTF-8 \
	TAIGA_SSL=False \
	TAIGA_HOSTNAME=localhost \
	TAIGA_SECRET_KEY="!!!REPLACE-ME-j1598u1J^U*(y251u98u51u5981urf98u2o5uvoiiuzhlit3)!!!" \
	TAIGA_DB_NAME=postgres \
	TAIGA_DB_USER=postgres

RUN python manage.py collectstatic --noinput \
	&& locale -a \
	&& ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

COPY [checkdb.py, docker-entrypoint.sh, /]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
