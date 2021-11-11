FROM phusion/baseimage:0.9.16
MAINTAINER Kierran McPherson <kierranm@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

EXPOSE 6667

# install the required packages
RUN apt-get update && sudo apt-get install -y ngircd

VOLUME /ngircd

# add the startup config file
RUN mkdir -p /etc/my_init.d
ADD Assets/config.sh /etc/my_init.d/config.sh
RUN chmod +x /etc/my_init.d/config.sh

# add ngircd to runit
RUN mkdir /etc/service/apache
ADD Assets/ngircd.sh /etc/service/ngircd/run
RUN chmod +x /etc/service/ngircd/run

# use phusion/baseimage init system
CMD ["/sbin/my_init"]
