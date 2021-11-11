FROM openjdk:8-jre

ENV SWARM_EXECUTORS 2
ENV SWARM_LABELS linux
ENV SWARM_NAME jenkins-linux
ENV SWARM_VERSION 3.14
ENV HOME /home/jenkins

RUN groupadd -g 233 docker \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      apt-transport-https \
      ca-certificates \
      gnupg2 \
      software-properties-common \
 && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - \
 && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" \
 && apt-get update \
 && apt-get install -y \
      curl \
      docker-ce \
      git \
      openssh-client \
      python3-pip \
      xvfb \
      libxss1 \
      gconf2 \
      libasound2 \
 && rm -rf /var/lib/apt/lists/* \
 && pip3 install --no-cache-dir awscli \
 && echo "\nVERSIONS INSTALLED:\n" \
 && aws --v \
 && docker -v \
 && python --version \
 && python3 --version \
 && pip3 -V

RUN groupadd -g 9999 jenkins \
    && useradd -r -u 9999 -g jenkins jenkins \
    && usermod -a -G docker jenkins

RUN mkdir -p $HOME \
 && curl --create-dirs -sSLo $HOME/swarm-client-$SWARM_VERSION.jar https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/$SWARM_VERSION/swarm-client-$SWARM_VERSION.jar \
 && chown -R jenkins:jenkins $HOME
USER jenkins

RUN git config --global user.email "jenkins@jenkins.com" \
 && git config --global user.name "Leroy Jenkins"

CMD ["sh", "-c", "java -jar $HOME/swarm-client-$SWARM_VERSION.jar -master \"$SWARM_MASTER\" -executors $SWARM_EXECUTORS -labels \"$SWARM_LABELS\" -name \"$SWARM_NAME\" -fsroot \"$HOME\""]
