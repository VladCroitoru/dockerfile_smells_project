FROM ubuntu
MAINTAINER hobbyqhd “liubingxin1030@outlook.com”
ENV REFRESHED_AT 2017_06_14
# RUN apt-get update
# RUN apt-get -y -q install nginx
# RUN apt-get -y install vim
# RUN mkdir -p /var/www/html
# ADD nginx/global.conf /etc/nginx/conf.d/
# ADD nginx/nginx.conf /etc/nginx/nginx.conf
# EXPOSE 80

RUN apt-get update -qq && apt-get install -qqy curl wget vim
# RUN curl https://get.docker.io/gpg | apt-key add gpg
RUN wget https://get.docker.io/gpg
RUN apt-key add gpg
RUN echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list
RUN apt-get install apt-transport-https
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:webupd8team/java

RUN apt-get update -qq && apt-get install -qqy iptables ca-certificates lxc openjdk-9-jre git-core lxc-docker

ENV JENKINS_HOME /opt/jenkins/data
ENV JENKINS_MIRROR http://mirrors.jenkins-ci.org

RUN mkdir -p $JENKINS_HOME/plugins
RUN curl -sf -o /opt/jenkins/jenkins.war -L $JENKINS_MIRROR/war-stable/latest/jenkins.war

RUN for plugin in chucknorris greenballs scm-api git-client git ws-cleanup;\
  do curl -sf -o $JENKINS_HOME/plugins/${plugin}.hpi \
    -L  $JENKINS_MIRROR/plugins/${plugin}/latest/${plugin}.hpi ; done
    
ADD ./dockerjenkins.sh /usr/local/bin/dockerjenkins.sh
RUN chmod +x /usr/local/bin/dockerjenkins.sh

VOLUME /var/lib/docker

EXPOSE 8080

ENTRYPOINT [ "/usr/local/bin/dockerjenkins.sh" ]
