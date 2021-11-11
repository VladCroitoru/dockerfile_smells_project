FROM openjdk:8-jre

MAINTAINER Nauman Badar

# set correct time zone. In my case it is Stockholm. This is a temporary fix until docker fixes the issue of always getting container with UTC timezone.
RUN echo Europe/Stockholm | tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata \

# some usefull command aliases
&& echo "alias ll='ls -la'" >> /root/.bashrc \
&& echo "alias l=ls" >> /root/.bashrc

