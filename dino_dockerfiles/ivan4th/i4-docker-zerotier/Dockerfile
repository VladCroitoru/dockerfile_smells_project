# Based on https://github.com/davide/docker-zerotier/blob/master/Dockerfile
FROM ubuntu:xenial

MAINTAINER Ivan Shvedunov <ivan4th@gmail.com>

COPY zt-gpg-key /tmp/
RUN echo "deb http://download.zerotier.com/debian/xenial xenial main" >/etc/apt/sources.list.d/zerotier.list
RUN apt-key add /tmp/zt-gpg-key
RUN apt-get update && apt-get install -y curl gnupg
RUN apt-get install -y zerotier-one
RUN tar -C / -cvf /zerotier.tar var/lib/zerotier-one

EXPOSE 9993/udp

COPY entrypoint.sh /
CMD ["/entrypoint.sh"]
