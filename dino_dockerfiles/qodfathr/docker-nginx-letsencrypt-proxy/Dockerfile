FROM annixa/docker-nginx-letsencrypt-proxy
MAINTAINER "Todd Mancini" <todd.mancini@daxat.com>
RUN apt-get -y update
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install virtualenv>=15.1.0
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
COPY letsencrypt-run.sh /opt
RUN chmod +x /opt/letsencrypt-run.sh
COPY nginx.conf /etc/nginx
COPY wellknown.conf /etc/nginx/sites-available
COPY webapp.2.conf /etc/nginx/sites-available

WORKDIR /opt
CMD ["/docker-entrypoint.sh"]
