FROM ubuntu:trusty
MAINTAINER Justin Menga <justin.menga@gmail.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# Set mirrors to NZ
# RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list 

# Install Python runtime
RUN apt-get update && \
    apt-get install -qyy \
      -o APT::Install-Recommends=false -o APT::Install-Suggests=false \
      python python-virtualenv python-mysqldb libpython2.7

# Create virtual environment
# Upgrade PIP in virtual environment to latest version
# Install Boto
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
