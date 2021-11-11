#docker-mediawiki
#Dockerfile for building an image from debian:jessie with mediawiki and nginx

FROM debian:jessie

#Set non-interactive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_PRIORITY critical
ENV DEBCONF_NOWARNINGS yes

#Update base system and install required packages
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" | tee /etc/apt/sources.list.d/nginx-mainline.list
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A
RUN echo "deb http://repo.percona.com/apt jessie main" | tee /etc/apt/sources.list.d/percona.list
RUN apt-get update && apt-get upgrade -y && apt-get install -y percona-server-server-5.6 percona-server-client-5.6 nginx php5-fpm php5 php5-dev php-pear php5-gd php5-mysql php5-curl php-apc php5-intl imagemagick php5-cli

