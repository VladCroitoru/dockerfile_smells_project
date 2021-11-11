FROM nginx:1.11.10

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list

RUN apt-get update && \
    apt-get -y install certbot -t jessie-backports && \
    apt-get -y install apache2-utils

RUN mkdir -p /var/www/fillyourday

COPY ./conf/ /etc/nginx/
COPY ./app.conf /etc/nginx/conf.d/
COPY ./cert/ /etc/letsencrypt/live/fillyourday.com/
COPY ./start.sh .

RUN chmod +x ./start.sh

ENTRYPOINT ["./start.sh"]