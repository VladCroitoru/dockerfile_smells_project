FROM ubuntu:trusty
MAINTAINER Anshul Sharma <optimisticanshul@gmail.com>

# prevent dkpg errors
ENV TERM=xterm-256color

# Install Python runtime

RUN apt-get update && \
    apt-get install -y \
   -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
   python python-virtualenv libpython2.7 python-mysqldb

# Create virtual environment
# Upgrade PIP in virtual environment to latest version
# Because of Bourne shell (sh) use dot operator to activate the environment
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

LABEL application=todobackend
