FROM phusion/baseimage:0.9.11
MAINTAINER needo <needo@superhero.org>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

RUN apt-get update -q

# Install Dependencies
RUN apt-get install -qy python wget git

# Install lazylibrarian from github
RUN git clone https://github.com/DobyTang/LazyLibrarian.git /opt/lazylibrarian
RUN chown nobody:users /opt/lazylibrarian

EXPOSE 8085

# lazylibrarian Configuration
VOLUME /config

# Downloads directory
VOLUME /downloads

# Movies directory
VOLUME /books

# Add edge.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD edge.sh /etc/my_init.d/edge.sh
RUN chmod +x /etc/my_init.d/edge.sh

# Add lazylibrarian to runit
RUN mkdir /etc/service/lazylibrarian
ADD lazylibrarian.sh /etc/service/lazylibrarian/run
RUN chmod +x /etc/service/lazylibrarian/run
