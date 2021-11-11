FROM openjdk:8
MAINTAINER Janne Rönkkö <janne.ronkko@vincit.fi>


RUN \
  useradd -d /home/jenkins -m -u 1000 jenkins

RUN \
  curl -sL https://deb.nodesource.com/setup_6.x | bash - \
  && apt-get install -y \
    build-essential \
    maven \
    nodejs
