FROM debian:latest

MAINTAINER  Agnaldo Marinho "agnaldoneto@ufpa.br"
MAINTAINER  Giuseppe Dal Maso "giuseppe@ufpa.br"

COPY sources.list /etc/apt/sources.list

RUN apt-get update; apt-get -y install php-fpm php-mysql php-cli php-json php-curl php-xsl; apt-get clean 

RUN rm -rf /var/lib/apt/lists/*

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-fpm.conf 

RUN usermod -u 1000 www-data

EXPOSE 9000

CMD ["php-fpm7.0", "-F"]
