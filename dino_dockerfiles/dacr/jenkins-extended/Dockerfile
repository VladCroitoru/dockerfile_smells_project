FROM library/jenkins

USER root

RUN apt-get update \
 && apt-get install -y git subversion \
 && apt-get install -y zip unzip tar  \
 && apt-get install -y python-pip \
 && apt-get install -y python-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install shade \
 && pip install ansible

#because of https://issues.jenkins-ci.org/browse/JENKINS-31089 :
RUN sed -i "s/jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024/jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 512/g" \
   /etc/java-8-openjdk/security/java.security

RUN apt-get update \
 && apt-get install -y proxytunnel \
 && rm -rf /var/lib/apt/lists/*

# Install docker but daemon won't be started of course
#RUN curl -sSL https://get.docker.com/ | sh
#RUN curl -L https://github.com/docker/compose/releases/download/1.5.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
# && chmod +x /usr/local/bin/docker-compose

USER jenkins

COPY plugins.txt /plugins.txt
RUN /usr/local/bin/plugins.sh /plugins.txt

