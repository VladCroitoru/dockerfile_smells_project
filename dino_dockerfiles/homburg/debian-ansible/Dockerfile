FROM debian:wheezy

MAINTAINER Thomas B Homburg <thomas@homburg.dk>

# Using instructions from https://devopsu.com/guides/ansible-ubuntu-debian.html
RUN apt-get update
RUN apt-get -qy install python-pip python-dev git
RUN pip install PyYAML jinja2 paramiko

# Install ansible
RUN pip install ansible==1.7
