FROM ubuntu:trusty

MAINTAINER Bilal Sheikh <bilal@techtraits.com>

RUN apt-get update && apt-get -y upgrade && apt-get -y install software-properties-common && add-apt-repository ppa:webupd8team/java -y && apt-get update

RUN (echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections) && apt-get install -y oracle-java8-installer oracle-java8-set-default

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV PATH $JAVA_HOME/bin:$PATH


# apparmor is required to run docker server within docker container
RUN apt-get update -qq && apt-get install -qqy wget curl git iptables ca-certificates apparmor

ENV JENKINS_SWARM_VERSION 1.26
ENV HOME /home/jenkins-slave


RUN useradd -c "Jenkins Slave user" -d $HOME -m jenkins-slave
RUN curl --create-dirs -sSLo $HOME/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar

ADD cmd.sh /cmd.sh

# set our wrapper
ENTRYPOINT ["/usr/local/bin/docker-wrapper"]

# setup our local files first
ADD docker-wrapper.sh /usr/local/bin/docker-wrapper

# now we install docker in docker - thanks to https://github.com/jpetazzo/dind
# We install newest docker into our docker in docker container
ADD https://get.docker.io/builds/Linux/x86_64/docker-latest /usr/local/bin/docker
RUN chmod +x /usr/local/bin/docker
RUN chmod +x /usr/local/bin/docker-wrapper

# Install Docker Compose
ADD https://github.com/docker/compose/releases/download/1.5.2/docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

VOLUME /var/lib/docker

#ENV JENKINS_USERNAME jenkins
#ENV JENKINS_PASSWORD jenkins
#ENV JENKINS_MASTER http://jenkins:8080

CMD /bin/bash /cmd.sh
