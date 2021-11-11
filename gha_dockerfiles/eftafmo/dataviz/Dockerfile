FROM node:16 AS frontend

ENV APP_HOME=/var/local/dataviz

RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME
ADD package.json package-lock.json postcss.config.js ./
RUN npm install --no-optional
ADD . $APP_HOME
RUN NODE_ENV=production npm run build


FROM python:3.9-slim-buster

# roles:
#   front - publishes ports to the world; this depends on run/docker-compose though...

LABEL maintainer="andrei.melis@eaudeweb.ro" \
      roles="front" \
      name="web"

#RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list

ENV APP_HOME=/var/local/dataviz \
    PYTHONUNBUFFERED=1

RUN runDeps="netcat-traditional" \
 && apt-get update -y \
 && apt-get install -y --no-install-recommends $runDeps \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir -p $APP_HOME \
 && mkdir -p /var/local/logs \
 && touch ~/.bashrc

WORKDIR $APP_HOME
COPY ./docker/entrypoint.sh ./docker/import.sh /bin/
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD . $APP_HOME
COPY ./docker/localsettings.py $APP_HOME/dv/
COPY --from=frontend /var/local/build /var/local/build
ENTRYPOINT ["entrypoint.sh"]
