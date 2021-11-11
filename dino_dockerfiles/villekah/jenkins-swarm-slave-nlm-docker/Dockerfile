FROM java:latest

MAINTAINER Petri Sirkkala <sirpete@iki.fi>

USER root

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN \
  apt-get update && \
  apt-get install \
    apt-transport-https && \
  apt-get -y install \
    build-essential \
    iceweasel \
    git \
    maven \
    rsync \
    locales \
    sudo \
    x11vnc \
    Xvfb && \
  update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java && \
  rm -rf /var/lib/apt/lists/* # 2015-11-13

# From: https://registry.hub.docker.com/u/selenium/node-base/dockerfile/
#===============
# Google Chrome
#===============
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/*

#==================
# Chrome webdriver
#==================
ENV CHROME_DRIVER_VERSION 2.14
RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

# Leiningen
ENV LEIN_ROOT 1
RUN curl -L -s https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > \
    /usr/local/bin/lein \
 && chmod 0755 /usr/local/bin/lein \
 && lein upgrade

# Node
# Install Node.js, Bower, Grunt, Gulp
RUN \
  curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
  apt-get -y install nodejs && \
  npm install -g npm@2.5.1 && \
  npm install -g bower@1.3.12 && \
  npm install -g grunt-cli@0.1.13 && \
  npm install -g gulp@3.8.11 && \
  echo 'export PATH="node_modules/.bin:$PATH"' >> /root/.bashrc && \
  echo 'export PATH="node_modules/.bin:$PATH"' >> /etc/skel/.bashrc && \
  chmod o+w -R /usr/local # Allow write for npm installs -g # 2015-11-13

ENV JENKINS_SWARM_VERSION 1.22
ENV HOME /home/jenkins-slave

RUN \
  useradd -c "Jenkins Slave user" -d $HOME -m jenkins-slave && \
  usermod -a -G sudo jenkins-slave && \
  echo "jenkins-slave ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/jenkins-slave && \
  curl --create-dirs -sSLo /usr/share/jenkins/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar \
    https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar && \
  chmod 755 /usr/share/jenkins

# Set the locale
RUN \
  echo "LANG=en_US.UTF-8" > /etc/default/locale && \
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
  locale-gen

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV JAVA_OPTS -Duser.country=US -Duser.language=en

# Set the timezone
RUN \
  ln -sf /usr/share/zoneinfo/Europe/Helsinki /etc/localtime
ENV TZ Europe/Helsinki

USER jenkins-slave

COPY jenkins-slave.sh /usr/local/bin/jenkins-slave.sh
COPY bowerrc /home/jenkins-slave/.bowerrc

VOLUME /home/jenkins-slave

WORKDIR /home/jenkins-slave

ENTRYPOINT ["/usr/local/bin/jenkins-slave.sh"]
