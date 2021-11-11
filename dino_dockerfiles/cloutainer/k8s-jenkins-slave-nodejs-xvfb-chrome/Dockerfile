FROM cloutainer/k8s-jenkins-slave-base:v24

#
# BASE PACKAGES
#
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/* && \
    apt-get -qqy update \
    && apt-get -qqy --no-install-recommends install \
    xvfb \
    pulseaudio \
    ffmpeg \
    g++ \
    build-essential \
    dbus \
    dbus-x11

#
# NODEJS
#
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get update -qqy && apt-get -qqy install -y nodejs && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

#
# KUBERNETES CLI (kubectl)
#
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

#
# CHROME
#
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update -qqy && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable} && \
    rm /etc/apt/sources.list.d/google-chrome.list && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/* && \
    ln -s /usr/bin/google-chrome /usr/bin/chromium-browser


#
# YARN
#
RUN wget -q -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
    apt-get update -qqy && apt-get -qqy install yarn && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*


#
# DBUS
#
COPY dbus-system.conf /tmp/dbus-system.conf
RUN mkdir /var/run/dbus/ && \
    chown -R jenkins:jenkins /var/run/dbus/


#
# INSTALL AND CONFIGURE
#
COPY docker-entrypoint-hook.sh /opt/docker-entrypoint-hook.sh
RUN chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint-hook.sh && \
    mkdir /tmp/.X11-unix | true && \
    chown -R root:root /tmp/.X11-unix && \
    chmod 1777 /tmp/.X11-unix

#
# PRINT VERSION OUTPUT
#
RUN echo "node version" && node -v && \
    echo "npm version" && npm -v && \
    echo "yarn version" && yarn -v && \
    echo "chrome version" && google-chrome --version

#
# RUN
#
USER jenkins
