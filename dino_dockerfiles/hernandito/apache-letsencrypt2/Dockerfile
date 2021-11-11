FROM linuxserver/baseimage.apache
MAINTAINER hernandito

# copy sources.list
COPY sources.list /etc/apt/

ENV APTLIST="libapache2-mod-php5 wget mc inotify-tools php5-gd php5-sqlite php5-mcrypt php5-tidy php5-mysql libapache2-mod-proxy-html"

# install main packages
RUN apt-get update -q && \
apt-get install $APTLIST -qy && \

# cleanup
apt-get clean -y && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD config/ /root/

ADD firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/my_init.d/firstrun.sh

ADD certbot-auto /usr/bin/certbot-auto
RUN chmod +x /usr/bin/certbot-auto
RUN mkdir -p /etc/letsencrypt

#ADD https://dl.eff.org/certbot-auto /usr/bin/certbot-auto
#RUN chmod a+x /usr/bin/certbot-auto

# add some files
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run /etc/service/*/finish /etc/my_init.d/*.sh

# Update apache configuration with this one
RUN a2enmod proxy proxy_http proxy_ajp rewrite deflate substitute headers proxy_balancer proxy_connect proxy_html xml2enc authnz_ldap

RUN apt-get update
RUN certbot-auto --noninteractive --os-packages-only

# ports and volumes
EXPOSE 80 443
VOLUME /config /etc/letsencrypt
ENV YOUR_EMAIL=
ENV SINGLE_DOMAIN=
ENV YOUR_DOMAIN=




