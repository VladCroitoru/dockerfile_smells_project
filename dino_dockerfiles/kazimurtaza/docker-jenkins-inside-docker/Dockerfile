#
# Jenkins + Dockers Inside
#
# https://github.com/kazimurtaza/docker-jenkins-inside-docker
#

# Pull base image.
FROM ubuntu:16.04

#
RUN \
apt update && \
apt install docker.io wget -y && \
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | apt-key add - && \
echo deb http://pkg.jenkins.io/debian-stable binary/ | tee /etc/apt/sources.list.d/jenkins.list

RUN \
apt update && \
apt install jenkins -y && \
service jenkins enable && \
service jenkins status


# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
