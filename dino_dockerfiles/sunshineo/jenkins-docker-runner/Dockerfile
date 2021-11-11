FROM ubuntu:16.04
EXPOSE 22
RUN apt-get update

# https://docs.docker.com/engine/installation/linux/ubuntulinux/
RUN apt-get install -qq apt-transport-https ca-certificates
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" > /etc/apt/sources.list.d/docker.list
RUN apt-get update
# This is recommended to use aufs storage drive. But I cannot figure out how to make it work
# uname does not work http://stackoverflow.com/questions/38003194/verfiy-the-version-of-ubuntu-running-in-a-docker-container
# RUN apt-get install -qq linux-image-extra-$(uname -r) linux-image-extra-virtual
RUN apt-get install -qq docker-engine

# https://www.digitalocean.com/community/tutorials/how-to-install-java-on-ubuntu-with-apt-get
RUN apt-get install -qq default-jre

# https://help.ubuntu.com/lts/serverguide/openssh-server.html
RUN apt-get install -qq openssh-server

ADD ./entrypoint.sh /
ENV JENKINS_PASSWORD jenkins
ENTRYPOINT ["/entrypoint.sh"]

VOLUME /var/lib/docker

CMD ["tail", "-f", "/var/log/docker.log"]