# this same shows how we can extend/change an existing official image from Docker Hub
FROM ubuntu:16.04
# Basic Meta data about the Image maintainers
MAINTAINER Daniel Aboyewa lolubyte.it@gmail.com

#prevent dpkg error
ENV TERM=xterm-256color

#Set  mirrors to the closet  mirror to me
# Install Python runtime
RUN apt-get update --fix-missing
RUN apt-get install -y software-properties-common
RUN apt-get install -y vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN  apt-get update && \
     apt-get install -y  \
     -o APT::Install-Recommended=false -o APT::Install-Suggests=false \
     build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -qy libmysqlclient-dev
#create virtual environment and also upgrade PIP in the virtual environment to the latest version
RUN python3.6 -m pip install virtualenv
RUN python3.6 -m virtualenv /appenv && \
    . /appenv/bin/activate && \
    python3.6 -m pip install pip --upgrade 

#  Adding entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
LABEL application=pollsend
