FROM ubuntu:14.04
MAINTAINER Peter Ericson <pdericson@gmail.com>

RUN apt-get update && \
apt-get install --no-install-recommends -y ca-certificates curl && \
rm -rf /var/lib/apt/lists/*

# https://github.com/Yelp/dumb-init
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && chmod +x /usr/local/bin/dumb-init

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
echo deb http://repos.mesosphere.io/ubuntu trusty main > /etc/apt/sources.list.d/mesosphere.list && \
apt-get update && \
apt-get install --no-install-recommends -y mesos=0.28.1-2.0.20.ubuntu1404 && \
rm -rf /var/lib/apt/lists/*

RUN apt-get remove -y --auto-remove openjdk* && \
    apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections && \
    sudo apt-get install -y oracle-java8-installer oracle-java8-set-default && \
    rm -r /var/cache/oracle-jdk* && \
    apt-get clean && apt-get autoremove -y

# Update the base ubuntu image with dependencies needed for Spark
RUN apt-get install -y python libnss3 curl && \
    apt-get autoremove -y


# http://docs.docker.com/installation/ubuntulinux/
RUN curl -fLsS https://get.docker.com/ | sh && test -x /usr/bin/docker

CMD ["/usr/sbin/mesos-slave"]

ENV MESOS_WORK_DIR /tmp/mesos
ENV MESOS_CONTAINERIZERS docker,mesos

# https://mesosphere.github.io/marathon/docs/native-docker.html
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins

# https://issues.apache.org/jira/browse/MESOS-4675
ENV MESOS_SYSTEMD_ENABLE_SUPPORT false

VOLUME /tmp/mesos

COPY entrypoint.sh /

ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]
