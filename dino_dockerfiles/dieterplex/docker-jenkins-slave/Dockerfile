FROM ubuntu:12.04
MAINTAINER Dieter Hsu "dieterplex@gmail.com"

# Set the env variables to non-interactive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_PRIORITY critical
ENV DEBCONF_NOWARNINGS yes

# Upstart and DBus have issues inside docker. Work around it
#RUN dpkg-divert --local --rename --add /sbin/initctl && ln -s /bin/true /sbin/initctl

# Installing the build environment
#RUN apt-get install -y build-essential devscripts fakeroot quilt dh-make automake libdistro-info-perl less nano python-dev

# Trick to Install fuse(openjdk7 dependency) because of container permission issue.
#RUN apt-get -y install fuse || true
#RUN rm -rf /var/lib/dpkg/info/fuse.postinst
#RUN apt-get -y install fuse
#RUN apt-get install -y openjdk-7-jdk && update-java-alternatives -s java-1.7.0-openjdk-amd64

RUN echo deb http://archive.ubuntu.com/ubuntu/ precise          main restricted universe multiverse >  /etc/apt/sources.list ; \
    echo deb http://archive.ubuntu.com/ubuntu/ precise-updates  main restricted universe multiverse >> /etc/apt/sources.list ; \
    echo deb http://archive.ubuntu.com/ubuntu/ precise-security main restricted universe multiverse >> /etc/apt/sources.list ; \
    apt-get update && apt-get -y install vim git openssh-server default-jre-headless python-pip

# Add jenkins user
RUN useradd -m -d /var/lib/jenkins -s /bin/bash -p $(openssl passwd -1 changeme) jenkins && \
    su - jenkins -c 'git config --global user.email "jenkins@yourdomain.com"' && \
    su - jenkins -c 'git config --global user.name "Jenkins"'
# Fix root passwd
RUN echo root:changeme | chpasswd
RUN apt-get clean && mkdir /var/run/sshd

