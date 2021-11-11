# Ubuntu Jenkins Slave with ChefDK and development tools

FROM hearstat/jenkins-slave-base:xenial
MAINTAINER Hearst Automation Team "atat@hearst.com"

RUN cd /tmp ;\
    wget -O chefdk.deb https://packages.chef.io/stable/ubuntu/12.04/chefdk_0.12.0-1_amd64.deb ;\
    dpkg -i chefdk.deb ;\
    rm -f /tmp/chefdk.deb

# Revert to Docker 1.9 until we upgrade the entire system
RUN apt-get update &&\
    apt-get install -y apt-transport-https ca-certificates && \
    apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
    echo "deb https://apt.dockerproject.org/repo/ ubuntu-wily main" | tee /etc/apt/sources.list.d/docker.list 
RUN apt-get update &&\
    apt-get install -y docker-engine=1.9.1-0~wily &&\
    apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Setup directories and rights so Jenkins user can do things without sudo
COPY systemconfig.sh /tmp/systemconfig.sh
RUN bash -c /tmp/systemconfig.sh

# Clean up mess
RUN rm -rf /tmp/* /var/tmp/*

COPY Gemfile $JENKINS_HOME/Gemfile

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

# Downgrade User
USER jenkins

WORKDIR $JENKINS_HOME
RUN chef exec bundle install
USER root

RUN locale-gen en_US.UTF-8
ENV LC_ALL="en_US.UTF-8" 
ENV LANG="en_US.UTF-8" 
ENV LANGUAGE="en_US.UTF-8"

CMD ["/usr/sbin/sshd", "-D"]
