FROM jenkins/jenkins:lts

EXPOSE 8080
EXPOSE 50000

USER root

RUN apt-get -y update
RUN apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"
RUN apt-get -y update
RUN apt-get -y install docker-ce
RUN systemctl enable docker
RUN adduser jenkins sudo
RUN usermod -a -G docker jenkins
RUN echo "jenkins  ALL=NOPASSWD: /usr/bin/docker, /usr/sbin/service" >> /etc/sudoers
RUN service docker start

USER jenkins

ENTRYPOINT [“/bin/tini”, “--“, “/usr/local/bin/jenkins.sh”]
