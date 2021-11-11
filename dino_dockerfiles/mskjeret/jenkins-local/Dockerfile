FROM jenkins/jenkins:lts

USER root
COPY data/ /var/jenkins_home/

RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl software-properties-common sudo && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && apt-key fingerprint 0EBFCD88 && \
     add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu zesty stable" && apt-get update && apt-get install -y docker-ce && rm -rf /var/lib/apt/lists/*

RUN usermod -a -G root jenkins
RUN adduser jenkins sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ADD entrypoint.sh /usr/local/bin
RUN chmod ugo+x /usr/local/bin/entrypoint.sh

# drop back to the regular jenkins
USER jenkins

ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/entrypoint.sh"]
