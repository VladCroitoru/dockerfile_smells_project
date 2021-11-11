FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install libltdl7 && addgroup docker --gid 999 && addgroup jenkins docker
RUN echo StrictHostKeyChecking no >> /etc/ssh/ssh_config

USER jenkins
