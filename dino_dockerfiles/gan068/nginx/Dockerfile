FROM nginx
MAINTAINER gan068<bleedkaga.ogre@gmail.com>

ENV TZ=Asia/Taipei

RUN apt-get update; apt-get install -y openssl; apt-get install -y vim

ADD ./nginx.conf /etc/nginx/
ADD ./sites/ /etc/nginx/sites-enabled/

RUN rm /etc/nginx/conf.d/default.conf

# default 80 443 ssl create
ADD ./scripts/make_ssl.sh /usr/local/bin/make_ssl.sh
RUN chmod a+x /usr/local/bin/make_ssl.sh
RUN /usr/local/bin/make_ssl.sh
