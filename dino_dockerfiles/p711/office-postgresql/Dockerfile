# using postgresql 12 because Gitlab expects >= 11
FROM postgres:12
MAINTAINER Ron Arts <ron.arts@p711.net>

#RUN locale-gen en_US.UTF-8  
#ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  

ADD init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh

