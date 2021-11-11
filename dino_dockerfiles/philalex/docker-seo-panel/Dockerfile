FROM ubuntu:14.04
MAINTAINER Philippe ALEXANDRE <alexandre.philippe+github@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
ENV ENV INITRD No
ENV DEBIAN_PRIORITY critical
ENV DEBCONF_NOWARNINGS yes

ENV DOMAIN_NAME www.acme.com

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y nginx php5-fpm php5-mysql python-pip git php5-curl php5-gd
RUN pip install envtpl
RUN mkdir -p /srv/www
WORKDIR /srv/www
RUN git clone https://github.com/sendtogeo/Seo-Panel.git
RUN chown -R www-data.www-data /srv/www/
ADD seo-panel.tpl /tmp/seo-panel.tpl

# nginx configuration
RUN envtpl -o /etc/nginx/sites-available/seo-panel.conf /tmp/seo-panel.tpl
RUN ln -s /etc/nginx/sites-available/seo-panel.conf /etc/nginx/sites-enabled/seo-panel
RUN rm /etc/nginx/sites-enabled/default
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Allow short tags in php
RUN sed -i 's/short_open_tag = Off/short_open_tag = On/g' /etc/php5/fpm/php.ini

ADD show.sh /tmp/show.sh
RUN chmod +x /tmp/show.sh
EXPOSE 80

CMD /tmp/show.sh && service php5-fpm start && nginx

