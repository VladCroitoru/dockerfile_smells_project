# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.22

RUN apt-get update --fix-missing
RUN apt-get install -y vim curl nmap postgresql-client redis-tools dnsutils mtr inetutils-traceroute net-tools telnet iputils-ping mongodb-clients parallel bonnie++

RUN echo "test6"

CMD ["/sbin/my_init"]
