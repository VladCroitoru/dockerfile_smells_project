FROM debian:8.4
MAINTAINER vrtulspud <email@domain.com>

# install lighttpd
RUN apt-get update && apt-get -y install \
	lighttpd \
&& apt-get clean autoclean \
&& apt-get autoremove \
&& rm -rf /var/lib/{apt,dpkg,cache,log}

# configure PHP with lighttpd
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf

EXPOSE 80

# start lighttpd
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
