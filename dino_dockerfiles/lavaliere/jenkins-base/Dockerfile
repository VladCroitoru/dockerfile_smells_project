# Docker base image for other CloudBees Jenkins images

FROM debian:jessie
MAINTAINER Andy Pemberton <apemberton@cloudbees.com>

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    openjdk-7-jdk \
    openssh-server \
    curl \
    ntp \
    ntpdate  \
    git  \
    maven  \
    less  \
    vim

RUN printf "AddressFamily inet" >> /etc/ssh/ssh_config 
ENV MAVEN_HOME /usr/bin/mvn
ENV GIT_HOME /usr/bin/git

# Install Docker client
RUN curl https://get.docker.io/builds/Linux/x86_64/docker-latest -o /usr/local/bin/docker
RUN chmod +x /usr/local/bin/docker
RUN groupadd docker

# Create Jenkins user
RUN useradd jenkins -d /home/jenkins
RUN echo "jenkins:jenkins" | chpasswd
RUN usermod -a -G docker jenkins

# Make directories for [masters] JENKINS_HOME, jenkins.war lib and [slaves] remote FS root, ssh privilege separation directory
RUN mkdir /usr/lib/jenkins /var/lib/jenkins /home/jenkins /var/run/sshd

# Set permissions
RUN chown -R jenkins:jenkins /usr/lib/jenkins /var/lib/jenkins /home/jenkins

# USER jenkins

CMD ["/bin/bash"]