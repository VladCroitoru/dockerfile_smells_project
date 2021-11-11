# Pull base image.
FROM mongo:3.6.1

LABEL name="Learning Locker docker image"

#update and run install script for Learning locker
RUN set -xe \
    && apt-get update \
	&& apt-get upgrade -y
	
RUN set -xe \
    && apt-get install -y \
	curl \
	git \
	git-core \
	python \
	make \
	automake \
	build-essential \
	xvfb \
	apt-transport-https \
	net-tools \
    wget \
	nginx

#install redis by hand
RUN apt-get install -y redis-server
#now add values to setup redis
RUN echo "maxmemory 128mb" >> /etc/redis/redis.conf
RUN echo "maxmemory-policy allkeys-lru" >> /etc/redis/redis.conf


RUN /etc/init.d/redis-server restart
RUN mkdir /var/log/mongo/ && chown -R mongodb:mongodb /var/log/mongo/
RUN /usr/local/bin/docker-entrypoint.sh mongod --fork --logpath /var/log/mongo/mongodb.log

COPY files/startup.js /usr/local/bin/startup.js

#wait for the DB to be started.
#RUN set -xe && mongo --nodb /usr/local/bin/startup.js 

 
RUN set -xe \
    && curl -o- -L http://lrnloc.kr/installv2 > deployll.sh \
	&& bash deployll.sh -y 3
	


COPY files/webapp.env /usr/local/learninglocker/current/webapp/.env
COPY files/xapi.env /usr/local/learninglocker/current/xapi/.env

COPY files/entrypoint.sh /entrypoint.sh 
RUN chmod +x /entrypoint.sh 

VOLUME ["/var/lib/mongodb"]

# Define default command.
ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]