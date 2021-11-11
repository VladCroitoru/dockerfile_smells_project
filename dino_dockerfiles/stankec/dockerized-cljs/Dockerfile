FROM openjdk:8-jdk

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nginx \
    && rm -rf /var/lib/apt/lists/* \
    && chown -R www-data:www-data /var/lib/nginx

COPY ./nginx.conf /etc/nginx/nginx.conf

ENV LEIN_ROOT true

RUN wget -q -O /usr/bin/lein \
    https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \
    && chmod +x /usr/bin/lein

RUN mkdir -p /app
WORKDIR /app

EXPOSE 80

CMD ["nginx"]
