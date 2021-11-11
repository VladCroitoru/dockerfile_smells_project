FROM java:8-jre

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common && \
    apt-get install -y wget curl git iptables ca-certificates && \
    apt-get install -y libssl-dev libffi-dev python-dev python-pip && \
    apt-get install -y ruby ruby-dev ruby-bundler && \
    apt-get clean

ENV JENKINS_SWARM_VERSION 2.2
ENV HOME /home/jenkins-slave

# Add rancher-compose and ansible
ADD rancher-compose /usr/bin/rancher-compose
RUN chmod +x /usr/bin/rancher-compose
RUN pip install --upgrade git+git://github.com/ansible/ansible.git@devel

RUN useradd -c "Jenkins Slave user" -d $HOME -m jenkins-slave
RUN curl --create-dirs -sSLo $HOME/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar

ADD cmd.sh /cmd.sh

RUN update-ca-certificates -f

#ENV JENKINS_USERNAME jenkins
#ENV JENKINS_PASSWORD jenkins
ENV JENKINS_MASTER http://jenkins-master:8080

CMD /bin/bash /cmd.sh
