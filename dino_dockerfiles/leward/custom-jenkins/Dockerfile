
FROM jenkins
COPY plugins.txt /usr/share/jenkins/ref/
USER root
RUN curl -fsSL https://get.docker.com/ | sh
RUN usermod -aG docker jenkins
USER jenkins
