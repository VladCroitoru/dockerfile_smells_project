FROM nginx:alpine

RUN \
  echo "*** installing dependencies ***" && \
  apk update --no-cache && \
  apk upgrade --no-cache && \
  apk add openssl curl && \
  rm -rf /var/cache/apk/*

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./certs/ca.crt /usr/local/share/ca-certificates/root-ca.crt
COPY ./certs/*.crt /etc/nginx/certs/
RUN rm /etc/nginx/certs/ca.crt
COPY ./certs/*.key /etc/nginx/private/

RUN cat /usr/local/share/ca-certificates/root-ca.crt >> /etc/ssl/certs/ca-certificates.crt
