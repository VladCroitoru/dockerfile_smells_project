# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.10.0

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...

RUN apt-get update && \
apt-get install -y --no-install-recommends git coreutils rsync && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -s https://raw.githubusercontent.com/envkey/envkey-source/master/install.sh | bash

COPY 20_git_sync_setup.sh /etc/my_init.d/20_git_sync_setup.sh
RUN chmod +x /etc/my_init.d/20_git_sync_setup.sh

COPY git_sync.sh /opt/git_sync.sh
RUN chmod +x /opt/git_sync.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*