FROM ubuntu:latest
MAINTAINER Chris Sandulow <https://github.com/jfalken>

# Do updates
RUN apt-get update && apt-get upgrade -y && apt-get install -y python \
  python-dev \
  python-distribute \
  python-pip \
  build-essential \
  git \
  supervisor

# Get sick-beard source
RUN git clone https://github.com/midgetspy/Sick-Beard.git

# Install dependency
RUN pip install cheetah

# Where to put blackhole'd nzb files. Map this to a directory on your host.
VOLUME /blackhole

# default port for sickbeard
EXPOSE 8081

# Supervisor will watch the sickbeard process and restart it after updates
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]