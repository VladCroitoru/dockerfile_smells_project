# Python base image <https://hub.docker.com/_/python>
FROM python:3.10.0-alpine

# cookiecutter works with current working
WORKDIR /workdir

COPY ./requirements.txt /tmp/requirements.txt

RUN set -x && \
    apk add --no-cache git && \
    echo 'appuser:x:10001:10001::/tmp:/sbin/nologin' >> /etc/passwd && \
    echo 'appuser:x:10001:' >> /etc/group && \
    mkdir --mode=777 /.cookiecutter_replay /.cookiecutters && \
    pip3 install --no-cache-dir --requirement /tmp/requirements.txt && \
    cookiecutter --version && \
    rm /tmp/requirements.txt

# use an unprivileged user by default
USER appuser:appuser

ENTRYPOINT ["cookiecutter"]
