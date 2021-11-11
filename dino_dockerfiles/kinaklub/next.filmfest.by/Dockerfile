FROM kinaklub/filmfest-base:1.0
MAINTAINER Stas Rudakou "stas@garage22.net"

ARG requirements=prod.txt

ADD . /app/src/
ADD IMAGE_VERSION /app/IMAGE_VERSION
RUN /app/bin/pip install -r "requirements/$requirements"

ENV DJANGO_SETTINGS_MODULE filmfest.settings.prod

RUN /app/src/docker-entrypoint.py collectstatic --noinput
ENTRYPOINT ["/app/src/docker-entrypoint.py"]
