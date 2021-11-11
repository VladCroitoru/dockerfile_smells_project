FROM jenkinsci/jenkins:lts
MAINTAINER Erokhin Dmitry <nefariusmag@gmail.com>
USER root
# установка нужных программ для работы
RUN apt-get update -y && apt-get install -y python3 python3-pip zip sudo sshpass git python-pip curl php
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt && \
    rm /opt/requirements.txt
# Настройка сетевых правил
COPY ssh_config /etc/ssh/ssh_config
# установка плагинов для jenkins
COPY plugins.txt /plugins.txt
RUN /usr/local/bin/plugins.sh /plugins.txt
RUN wget -q https://releases.hashicorp.com/packer/1.1.3/packer_1.1.3_linux_amd64.zip && \
    unzip packer_1.1.3_linux_amd64.zip && mv packer /bin/packer
# Скачиваем новейшую версию
# RUN wget -q http://updates.jenkins-ci.org/latest/jenkins.war -O /usr/share/jenkins/jenkins.war
USER jenkins
# настройка общих параметров и запуск приложения
RUN git config --global user.email "nefariusmag@gmail.com"
RUN git config --global user.name "Erokhin Dmitry"
VOLUME ["/var/jenkins_home"]
EXPOSE 8080
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
