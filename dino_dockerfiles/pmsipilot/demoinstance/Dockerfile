FROM ubuntu:16.04
MAINTAINER Loïc PORTE
RUN apt-get update && apt-get install -y git python python-dev\
 python-pip mysql-client libmysqlclient-dev nodejs npm\
  libldap2-dev libsasl2-dev libssl-dev nginx supervisor
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN rm -rf /etc/nginx/sites-available/* /etc/nginx/sites-enabled/*

COPY ./ressources/nginx/nginx-server /etc/nginx/sites-available/default
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log


RUN mkdir -p /etc/demoinstance/instance_image/
RUN mkdir /opt/demoinstance 
COPY ./ /opt/demoinstance

WORKDIR /opt/demoinstance/frontend
RUN npm install
RUN node_modules/gulp/bin/gulp.js


WORKDIR /opt/demoinstance/backend/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN python setup.py install

COPY ./ressources/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

EXPOSE 8080
