# phusion dump
# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
FROM phusion/baseimage:0.9.9
#FROM ubuntu

# Use baseimage-docker's init system + bash.
# ENTRYPOINT ["/sbin/my_init"]
# CMD ["-- bash -l"]
CMD ["/sbin/my_init"]

# ...put your own build instructions here...

RUN apt-get update
RUN apt-get install -y libssl-dev git-core libgnutls28-dev lua5.1 liblua5.1-0 liblua5.1-0-dev screen python-dev python-pip bzip2 zlib1g-dev make curl unzip wget flex autoconf 

# Fix dnsmasq bug (see https://github.com/nicolasff/docker-cassandra/issues/8#issuecomment-36922132)
RUN echo 'user=root' >> /etc/dnsmasq.conf

# Setup system for the archiveteam autoscript
RUN adduser --system --group --shell /bin/bash archiveteam

# Install dependencies [phase 2]
RUN pip install seesaw
RUN pip install seesaw requests
RUN pip install --upgrade seesaw requests


# Clean up APT when done.
RUN apt-get autoremove
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*