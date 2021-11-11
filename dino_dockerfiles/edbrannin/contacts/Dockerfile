FROM leafney/docker-flask:py2
MAINTAINER Ed Brannin "edbrannin@gmail.com"
WORKDIR /app/web
RUN apk update && \
    apk add py-pillow build-base python2-dev py-pip ca-certificates && \
    rm -rf /var/cache/apk/*

ENV FLASK_APP=contacts SIM_CONTACTS_SETTINGS=config.py FLASK_DEBUG=0

# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#add-or-copy
# Try not to invalidate the `pip install` step by copything everything else after
COPY requirements.txt /app/web/
RUN pip install --no-cache-dir -r requirements.txt && mkdir -p /app/web/instance

RUN rm /app/web/app.py
COPY . /app/web/
VOLUME ["/app/web/instance", "/app/web/db"]
