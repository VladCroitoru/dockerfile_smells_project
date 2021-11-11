FROM debian
MAINTAINER Guillaume Abrioux <guillaume@abrioux.info>

COPY ./ /var/www/pastefile
RUN apt-get update && apt-get install -y git nginx-full gettext-base python-setuptools python-dev gcc && easy_install pip && apt-get clean
RUN pip install -r /var/www/pastefile/requirements.txt
RUN mkdir /opt/pastefile && mkdir -p /opt/pastefile/files/ /opt/pastefile/tmp
RUN chown -R www-data:www-data /opt/pastefile

COPY ./extra/Docker/configs/nginx.conf.template /opt/pastefile/nginx.conf.template
COPY ./extra/Docker/configs/vhost.conf.template /opt/pastefile/vhost.conf.template
COPY ./extra/Docker/scripts/entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]
