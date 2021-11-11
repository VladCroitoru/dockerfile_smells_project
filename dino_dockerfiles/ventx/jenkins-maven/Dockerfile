FROM jenkins/jenkins
USER root
RUN apt-get update && \
apt-get install -y python-pip default-jdk docker apt-transport-https ca-certificates curl gnupg2 software-properties-common xmlstarlet maven && \
chown 1000 ~/ && \
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - && \ 
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable" && \
pip install awscli && \
apt-get update && \
apt-get -y install docker-ce
User 1000
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
