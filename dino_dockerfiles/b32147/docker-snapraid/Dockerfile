FROM linuxserver/baseimage
MAINTAINER LinuxServer.io <ironicbadger@linuxserver.io>

ENV APTLIST="snapraid python2.7 git"

# Install application
RUN add-apt-repository ppa:tikhonov/snapraid && \
    apt-get update -qq && \
    apt-get install $APTLIST -qy && \
    git clone https://github.com/b32147/snapraid-runner.git /app/snapraid-runner && \
    chmod +x /app/snapraid-runner/snapraid-runner.py && \
    apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

#Adding Custom files
ADD init/ /etc/my_init.d/
ADD cron/ /etc/cron.d/
RUN chmod -v +x /etc/service/*/run && chmod -v +x /etc/my_init.d/*.sh

VOLUME /mnt /config
