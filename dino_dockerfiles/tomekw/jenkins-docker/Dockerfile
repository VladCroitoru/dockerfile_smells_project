FROM docker:1.11.2

MAINTAINER Tomek Wałkuski <ja@jestem.tw>

WORKDIR /opt

ENV JENKINS_HOME /var/jenkins

VOLUME /var/jenkins

RUN apk --update --no-cache add git openjdk8-jre ttf-dejavu openssh-client py-pip \
    && wget http://mirrors.jenkins-ci.org/war/2.14/jenkins.war \
    && echo 'jenkins ALL=(ALL) NOPASSWD: /usr/local/bin/docker' >> /etc/sudoers \
    && pip install docker-compose

CMD ["java", "-jar", "/opt/jenkins.war"]
