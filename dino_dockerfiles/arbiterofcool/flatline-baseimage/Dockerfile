FROM phusion/baseimage:0.9.15
MAINTAINER Sean Chatman <xpointsh@gmail.com>

######### Installing Dependencies #########

RUN apt-get update
RUN apt-get install -y \
    curl \
    openjdk-7-jdk \
    unzip \
    wget \
    iptables \
    ca-certificates \
    lxc \
    python-pip

######### Installing Jenkins #########

RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" > /etc/apt/sources.list.d/jenkins.list
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y jenkins

VOLUME /var/lib/jenkins
VOLUME /var/lib/docker

RUN echo "/var/lib/jenkins" > /etc/container_environment/JENKINS_HOME

######### Installing Docker in Docker #########

# Install Docker from Docker Inc. repositories.
RUN apt-get install -y apt-transport-https
RUN echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
RUN apt-get update
RUN apt-get install -y lxc-docker

# Install fig
RUN pip install -U \
    fig \
    docker-py

######### Starting Daemons #########

# Install the Docker daemon.
RUN mkdir -p /etc/my_init.d/
ADD wrapdocker /etc/my_init.d/wrapdocker
RUN chmod +x /etc/my_init.d/wrapdocker

# Setup Jenkins daemon
ONBUILD RUN mkdir -p /etc/service/jenkins
ONBUILD ADD jenkins/run /etc/service/jenkins/run
ONBUILD RUN chmod +x /etc/service/jenkins/run

# Add jobs and plugins
ONBUILD RUN mkdir -p /var/lib/jenkins
ONBUILD ADD jobs /var/lib/jenkins/jobs
ONBUILD ADD plugins /var/lib/jenkins/plugins

ONBUILD RUN mkdir -p /var/lib/jenkins/jobs/pull-seed-job-on-startup/workspace

ONBUILD CMD ["/sbin/my_init"]