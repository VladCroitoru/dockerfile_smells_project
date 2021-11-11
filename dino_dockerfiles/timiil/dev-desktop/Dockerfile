FROM timiil/docker-ubuntu-vnc-desktop
MAINTAINER timiil@163.com

RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
   && apt-get update \
   && apt-get install -y software-properties-common \
   && add-apt-repository ppa:webupd8team/java \
   && apt-get update \
   && apt-get install -y oracle-java8-installer

RUN sudo apt-get install -y gedit nano eclipse eclipse-pde eclipse-jdt
