#FROM debian:7
FROM debian:buster

#RUN echo "deb http://archive.debian.org/debian wheezy main contrib non-free" > /etc/apt/sources.list

RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y build-essential libc6 gcc make bash valgrind

RUN mkdir -p /ft_ping

COPY Makefile /ft_ping/Makefile
COPY srcs /ft_ping/srcs
COPY includes /ft_ping/includes
COPY entrypoint.sh /ft_ping/entrypoint.sh
COPY srcs.mk /ft_ping/srcs.mk

RUN chmod +xw /ft_ping/entrypoint.sh

WORKDIR /ft_ping

ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
