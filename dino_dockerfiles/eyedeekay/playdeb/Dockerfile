FROM ubuntu:xenial
RUN echo "deb http://archive.getdeb.net/ubuntu xenial-getdeb games" > /etc/apt/sources.list.d/playdeb.list
ADD http://archive.getdeb.net/getdeb-archive.key getdeb-archive.key
RUN apt-key add getdeb-archive.key
RUN apt-get update
RUN apt-get install -y xdg-user-dirs xdg-utils liblz4-tool less
RUN apt-get -y dist-upgrade
RUN adduser --home /home/playdeb --disabled-password --gecos 'playdeb,,,,' playdeb
VOLUME /home/playdeb
RUN chown -R playdeb:playdeb /home/playdeb
ENTRYPOINT [ "sh", "-i", "-c" ]
