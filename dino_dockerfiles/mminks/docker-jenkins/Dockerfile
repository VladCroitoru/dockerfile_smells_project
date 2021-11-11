FROM openjdk:8-jdk

ENV JENKINS_VERSION 2.150.1
ENV JENKINS_SHA 0da17386e514499ad77d1976019853df9af3ccba
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000
ENV JENKINS_UC https://updates.jenkins-ci.org

ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log
ENV TZ=Europe/Berlin

RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" > /etc/apt/sources.list.d/ansible.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 \
    && apt-get update \
    && apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common \
    && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" \
    && apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install -y wget git curl zip ruby ruby-dev make gcc cron sudo ansible jq python-pip docker-ce \
    && systemctl disable docker \
    && echo manual | tee /etc/init/docker.override \
    && apt-get autoremove --purge -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/* \
    && /usr/bin/gem install bundler \
    && echo $TZ | sudo tee /etc/timezone \
    && sudo dpkg-reconfigure --frontend noninteractive tzdata  \
    && useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins \
    && mkdir -p /usr/share/jenkins/ref/init.groovy.d \
    && curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-static -o /bin/tini \
    && chmod +x /bin/tini \
    && echo "$TINI_SHA /bin/tini" | sha1sum -c - \
    && curl -fL http://mirrors.jenkins-ci.org/war-stable/$JENKINS_VERSION/jenkins.war -o /usr/share/jenkins/jenkins.war \
    && echo "$JENKINS_SHA /usr/share/jenkins/jenkins.war" | sha1sum -c - \
    && chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref

RUN wget "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && pip install awscli --upgrade --user \
    && wget $(curl -Ls https://releases.hashicorp.com/index.json | jq '{terraform}' | grep url | egrep linux_amd64 | sort -V | tail -n1 | awk '{print $2}' | sed 's/"*,*//g') -O /tmp/terraform.zip \
    && unzip /tmp/terraform.zip -d /usr/local/bin \
    && curl -s -L -o /usr/local/bin/docker-compose $(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r ".assets[] | select(.name | test(\"$(uname -s)-$(uname -m)\")) | .browser_download_url" | head -n1) \
    && chmod +x /usr/local/bin/docker-compose

VOLUME /var/jenkins_home

COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy

EXPOSE 8080
EXPOSE 50000

USER jenkins

COPY jenkins.sh /usr/local/bin/jenkins.sh

COPY jenkins.sudoers /etc/sudoers.d/jenkins

COPY plugins.sh /usr/local/bin/plugins.sh

ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
