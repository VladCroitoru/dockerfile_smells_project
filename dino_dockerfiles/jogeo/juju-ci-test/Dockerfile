FROM ubuntu:14.04
MAINTAINER John George <john.george@canonical.com>

RUN useradd -m ubuntu
RUN echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/juju-users
USER ubuntu

ENV HOME /home/ubuntu
ENV JUJU_HOME /home/ubuntu/.juju
ENV JUJU_REPOSITORY /home/ubuntu/repository

ADD setup.sh /setup.sh
RUN /setup.sh

VOLUME ["/home/ubuntu/.juju"]

ADD run.sh /run.sh
CMD /run.sh
