FROM ubuntu:trusty

MAINTAINER Lamberto Diwa <lambertodiwajr@gmail.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# Set mirrors to US
RUN sed -i "s/http:\/\/archive./http:\/\/us.archive./g" /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python python-virtualenv libpython2.7 python-mysqldb

# Create virtual environment
# Upgrade PIP in virtual environment to latest version
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

# Add label to be used when doing `make clean` command
LABEL application=todobackend
