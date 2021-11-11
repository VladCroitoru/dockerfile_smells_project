FROM ubuntu:trusty
MAINTAINER Nilesh Gule <vn_nilesh@yahoo.com>

# prevent dpkg errors
ENV TERM=xterm-256color

# set mirror to NZ
RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list

# Install python runtime
RUN apt-get update && \
    apt-get install -y \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python python-virtualenv libpython2.7 python-mysqldb

# Create virtual environment
# Upgrade pip in virtual environment to latest version
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

LABEL application=todobackend
