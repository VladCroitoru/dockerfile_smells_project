FROM ruby:2.2.5
LABEL org.freenas.interactive="false" \
      org.freenas.version="2.1" \
      org.freenas.upgradeable="true" \
      org.freenas.expose-ports-at-host="true" \
      org.freenas.autostart="true" \
      org.freenas.web-ui-protocol="http" \
      org.freenas.web-ui-port="3030" \
      org.freenas.web-ui-path="" \
      org.freenas.port-mappings="3030:3030/tcp" \
      org.freenas.volumes="[                    \
          {                                     \
              \"name\": \"/app/dashboards\",    \
              \"descr\": \"Dashboards\"         \
          },                                    \
          {                                     \
             \"name\": \"/app/hapush\",         \
             \"descr\": \"Hapush\"              \
          },                                    \
          {                                     \
             \"name\": \"/app/lib\",            \
             \"descr\": \"Lib\"                 \
          }                                     \
      ]"                                        \
      org.freenas.settings="[                   \
          {                                     \
              \"env\": \"HA_URL\",              \
              \"descr\": \"HA Server URL\",     \
              \"optional\": false               \
          },                                    \
          {                                     \
              \"env\": \"HA_KEY\",              \
              \"descr\": \"API Key for HA\",    \
              \"optional\": true                \
          },                                    \
          {                                     \
              \"env\": \"DASH_HOST\",           \
              \"descr\": \"Dashing Hostname\",  \
              \"optional\": true                \
          }                                     \
      ]"


MAINTAINER Jan Willhaus <mail@janwillhaus.de>

RUN apt-get update \
 && apt-get install -y \
      sqlite \
      nodejs \
      libpq-dev \
      libssl-dev \
      libsqlite3-dev \
      ruby-dev \
      python3 \
      python3-pip \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN gem install dashing \
 && gem install bundler \
 && bundle \
 && pip3 install daemonize sseclient beautifulsoup4 \
 && pip3 install --upgrade requests

EXPOSE 3030

VOLUME /app/lib /app/dashboards /app/hapush

ENV HA_URL=https://homeassistant
ENV HA_KEY=myapikey
ENV DASH_HOST=127.0.0.1:3030

ENTRYPOINT exec /app/hapush/hapush.py && dashing start
