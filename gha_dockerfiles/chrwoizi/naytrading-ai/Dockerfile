FROM tensorflow/tensorflow:latest
#FROM arm32v7/ubuntu:latest

# increase version to install security updates
RUN touch environment-v1

# install security updates
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install unattended-upgrades

# add user
RUN useradd -ms /bin/bash theuser
#RUN echo theuser:todopasswordhere | chpasswd
USER theuser
WORKDIR /home/theuser

COPY --chown=theuser:theuser / /home/theuser/naytrading-ai/

WORKDIR /home/theuser/naytrading-ai/src
