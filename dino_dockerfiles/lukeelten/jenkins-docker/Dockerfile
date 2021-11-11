FROM jenkins/jenkins:lts-slim
LABEL maintainer="Tobias Derksen <tobias.derksen@student.fontys.nl>"

USER root

RUN rm /var/lib/apt/lists/* -vf && apt-get -y update && apt-get -y install curl git sudo apt-transport-https ca-certificates curl gnupg2 software-properties-common apt-utils \
      && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add - \
      && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" \
      && apt-get -y update \
      && apt-get -y install docker-ce \
      && curl -L https://github.com/docker/compose/releases/download/1.27.4/docker-compose-`uname -s`-`uname -m` -o /usr/bin/docker-compose \
      && chmod +x /usr/bin/docker-compose \
      && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN gpasswd -a jenkins docker && echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt

VOLUME /var/jenkins_home
