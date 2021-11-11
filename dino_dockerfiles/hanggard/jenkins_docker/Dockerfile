FROM jenkins/jenkins:lts
LABEL maintainer "hanggard@gmail.com"
EXPOSE 8080 50000
USER root
RUN apt-get update && apt-get install -y apt-transport-https software-properties-common
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | tee -a /etc/apt/sources.list && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y python-pip python-dev sendmail-bin sendmail xvfb libyaml-dev jq build-essential libssl-dev libffi-dev yarn ansible
RUN pip install awscli
