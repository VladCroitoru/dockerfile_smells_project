FROM ubuntu:xenial
MAINTAINER Alex Sanz <asans@evirtualpost.com>

# expose the port
EXPOSE 8080
# required to make docker in docker to work
VOLUME /var/lib/docker

# default jenkins home directory
ENV JENKINS_HOME /var/jenkins
# set our user home to the same location
ENV HOME /var/jenkins

# set our wrapper
ENTRYPOINT ["/usr/local/bin/docker-wrapper"]
# default command to launch jenkins
CMD java -jar /usr/share/jenkins/jenkins.war

# setup our local files first
ADD docker-wrapper.sh /usr/local/bin/docker-wrapper

# for installing docker related files first
#RUN echo deb http://archive.ubuntu.com/ubuntu xenial universe > /etc/apt/sources.list.d/universe.list
# apparmor is required to run docker server within docker container
RUN apt-get update -qq && apt-get install -qy wget curl git iptables apt-transport-https ca-certificates apparmor software-properties-common

# now we install docker in docker - thanks to https://github.com/jpetazzo/dind
# We install newest docker into our docker in docker container
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"
RUN apt-get update -qq && apt-get -qqy install docker-ce docker-ce-cli containerd.io
#ADD https://get.docker.io/builds/Linux/x86_64/docker-latest.tgz /usr/local/bin/docker
#RUN chmod +x /usr/local/bin/docker

# for jenkins
RUN echo deb https://pkg.jenkins.io/debian binary/ >> /etc/apt/sources.list \
    && wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add -
RUN apt-get update -qq && apt-get install -qy openjdk-8-jdk jenkins
