# Lastest visono/debian_serf
FROM visono/debian_serf:latest

MAINTAINER Patrik Hagedorn <p.hagedorn@visono.com>

USER root

# Install Oracle Java 1.8 (Java8) and accept the license automatically
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list \
    && echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \
    && apt-get update -q \
    && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
    && apt-get install -qy \
        oracle-java8-installer \
        oracle-java8-set-default \
    && rm -rf /var/cache/oracle-jdk8-installer \
    && apt-get autoclean -y \
    && apt-get autoremove -y

CMD ["/bin/bash"]