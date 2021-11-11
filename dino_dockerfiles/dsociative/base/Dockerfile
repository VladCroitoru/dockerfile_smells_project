FROM        dockerfile/python
MAINTAINER  dsociative

VOLUME      /db
VOLUME      /log

RUN         ln -s -f /usr/share/zoneinfo/Europe/Moscow /etc/localtime

RUN         apt-get -y update
RUN         apt-get install -y redis-server mongodb-server nginx

RUN         pip install supervisor pyzmq
RUN         pip install 'https://github.com/dsociative/waitredis/archive/master.tar.gz'

CMD         ["/usr/local/bin/supervisord"]
