#Inherit from official PostgreSQL docker
FROM postgres:9.4

MAINTAINER Alexander Mustafin <mustfain.aleksandr@gmail.com>

#Import key for repo
RUN echo 'deb http://pkg.yeti-switch.org/debian/jessie stable main ext' >> /etc/apt/sources.list

#Install additional packages
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 9CEBFFC569A832B6 && \
    apt-get update && apt-get -y install postgresql-9.4-prefix postgresql-9.4-pgq3 postgresql-9.4-yeti

