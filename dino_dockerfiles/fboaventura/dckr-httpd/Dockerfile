FROM busybox

LABEL maintainer "Frederico Freire Boaventura <frederico@boaventura.net>"
LABEL version "1.0"

ENV DOMAIN "localhost"
ENV BASEDIR "/app/www"
ENV CONFDIR "/app/conf"
ENV PORT "80"

RUN mkdir -p /app/ssl /app/www /app/conf

ADD files/caddy /app/
ADD files/Caddyfile /app/conf/

CMD /app/caddy -agree -log=stdout -conf=/app/conf/Caddyfile -root=$BASEDIR
