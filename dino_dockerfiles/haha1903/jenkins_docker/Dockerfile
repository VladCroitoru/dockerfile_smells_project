FROM jenkins/jenkins:lts

USER root

RUN apt-get update
RUN apt-get -y install apt-transport-https ca-certificates curl software-properties-common build-essential libpng-dev
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs docker-ce
RUN npm config set registry https://registry.npm.taobao.org
RUN npm install -g gulp-cli
RUN npm install -g bower

ENV TZ=Asia/Shanghai

USER jenkins
