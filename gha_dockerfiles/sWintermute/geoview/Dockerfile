FROM alpine:3.12 AS build
ENV PYTHONUNBUFFERED 1
ENV SETUPTOOLS_USE_DISTUTILS stdlib

RUN mkdir -p /app
RUN apk add --no-cache python3 py3-pip postgresql-libs py3-wheel
RUN apk add --no-cache py3-numpy --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community
RUN if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi
RUN apk add --no-cache --virtual .build-deps postgresql-dev python3-dev build-base

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt && \
    pip uninstall virtualenv virtualenv-clone setuptools pip -y && \
    rm -rf /root/.cache /root/.local \
    /etc/apk/ /usr/share/apk/ /lib/apk/ /sbin/apk \
    /media /usr/lib/terminfo /usr/share/terminfo \
    /usr/lib/python*/ensurepip \
    /usr/lib/python*/turtledemo /usr/lib/python*/turtle.py /usr/lib/python*/__pycache__/turtle.* \
    /var/cache/apk \
    /var/lib/apk && \
    find /usr/lib/python*/site-packages/django/conf/locale ! -name __pycache__ ! -name __init__.py ! -name ru ! -name en -mindepth 1 -maxdepth 1  -type d -print0 | xargs -0 rm -rf && \
    find /usr/lib/python*/site-packages/django/contrib/admin/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf && \
    find /usr/lib/python*/site-packages/django/contrib/admindocs/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/auth/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/contenttypes/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/flatpages/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/gis/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/humanize/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/postgres/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/redirects/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/sessions/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf  && \
    find /usr/lib/python*/site-packages/django/contrib/sites/locale ! -name ru ! -name en* -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf && \
    find /usr/lib/python*/site-packages/ -name *.egg-info -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0 rm -rf && \
    find /usr/lib/python*/* | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf && \
    python3 -m compileall -q -b /usr/lib/python* && \
    find /usr/lib/python*/* -name "*.py"|xargs rm -rf&& \
    find /usr/lib/python*/* -name '*.c' -delete && \
    find /usr/lib/python*/* -name '*.pxd' -delete && \
    find /usr/lib/python*/* -name '*.pyd' -delete && \
    find /usr/lib/python*/* -name '__pycache__' | xargs rm -r && \
    rm -rf /app/requirements.txt* && \
    rm -rf /usr/lib/python*/site-packages/*.dist-info

FROM scratch AS deploy
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000 5678
COPY --from=build / /
WORKDIR /app

CMD ["./docker-entrypoint.sh"]