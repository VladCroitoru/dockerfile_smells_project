FROM jenkins:2.7.3
MAINTAINER Robert Brem <brem_robert@hotmail.com>
USER root
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates && \
    apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
    echo "deb https://apt.dockerproject.org/repo debian-jessie main" >> /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-engine=1.10.3-0~jessie && \
    gpasswd -a jenkins docker && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=true
RUN curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    apt-get update && \
    apt-get install -y sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY run.sh ./run.sh
ADD kubectl /usr/local/bin/
RUN chmod +x ./run.sh
ENTRYPOINT ["/bin/bash","-c","./run.sh"]
