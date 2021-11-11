FROM python:2.7-alpine

WORKDIR /webapps

LABEL CremeCRM=1.6

COPY requirements.txt .

RUN mkdir -p /webapps \
    && addgroup -g 1000 django \
    && adduser -u 1000 -G django -s /bin/sh -D django \
    # install depends
    && apk add --no-cache \
        zlib \
        graphviz \
        libpq  \
        libjpeg-turbo \
        openjdk7-jre-base \
    # build libs
    && apk add --no-cache --virtual .build-deps \
        binutils-gold \
        build-base \
        mercurial \
        graphviz-dev \
        postgresql-dev \
        zlib-dev \
    # get sources
    && hg clone https://bitbucket.org/hybird/creme_crm-1.6 creme_crm \
    # pip libs
    && LIBRARY_PATH=/lib:/usr/lib pip install -r requirements.txt \
    # add a link for gunicorn & wsgi applications
    && (cd /webapps/creme_crm/creme; ln -s django.wsgi wsgi.py) \
    # cleaning
    && apk del .build-deps \
    && rm -rf /root/.cache \
    && chown django:django /webapps/creme_crm -R

COPY gunicorn_settings.py .

# entry point en command
COPY entry_point.sh /
ENTRYPOINT ["/entry_point.sh"]
CMD ["gunicorn", "-c", "/webapps/gunicorn_settings.py", "wsgi:application" ]

