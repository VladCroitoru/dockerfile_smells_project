FROM python:3.4
MAINTAINER Quang <quang.astronaut@gmail.com>


ENV NGINX_VERSION 1.9.5
RUN apt-key adv \
  --keyserver hkp://pgp.mit.edu:80 \
  --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62

RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list
RUN apt-get update && apt-get upgrade -y
RUN set -x; \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        locales \
        ca-certificates \
        nginx sudo \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get install -y libpq-dev

# create user taiga
RUN useradd -m -d /home/taiga -p taiga -s /bin/bash taiga
RUN usermod -aG sudo taiga

# clone backend service
RUN sudo -H -u taiga git clone -b stable --single-branch https://github.com/taigaio/taiga-back.git /home/taiga/taiga-back &&\
   cd /home/taiga/taiga-back && pip install -r requirements.txt

# install slack integration
RUN pip install taiga_contrib_slack

# add configuration files
ADD config/local.py /home/taiga/taiga-back/settings/local.py

# clone frontend
RUN sudo -H -u taiga git clone https://github.com/taigaio/taiga-front-dist.git /home/taiga/taiga-front-dist
ADD config/conf.json /home/taiga/taiga-front-dist/dist/js/conf.json
RUN cd /home/taiga/taiga-front-dist/dist/js && sudo -H -u taiga wget https://github.com/taigaio/taiga-contrib-slack/raw/master/front/dist/slack.js

# nginx configuration
ADD config/nginx-taiga.conf /etc/nginx/conf.d/taiga.conf
RUN rm -f /etc/nginx/conf.d/default.conf

# fix locale
ADD config/locale.gen /etc/locale.gen
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales -f noninteractive tzdata
RUN echo "LANG=en_US.UTF-8\nLC_ALL=en_US.UTF-8\nLANGUAGE=en_US.UTF-8" >> /etc/default/locale
RUN echo 'LC_ALL=en_US.UTF-8\nLANG=en_US.UTF-8\nLANGUAGE=en_US.UTF-8' >> /etc/environment


ADD scripts/start.sh /usr/local/docker/scripts/start.sh
ADD scripts/main.sh /usr/local/docker/scripts/main.sh
RUN chmod 755 /usr/local/docker/scripts/start.sh
RUN mkdir /home/taiga/logs
RUN touch /home/taiga/.noready
RUN chown taiga: -R /home/taiga/

EXPOSE 80

ENV USER root
ENTRYPOINT ["/usr/local/docker/scripts/start.sh"]
