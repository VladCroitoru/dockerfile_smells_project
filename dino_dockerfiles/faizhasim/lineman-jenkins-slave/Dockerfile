FROM dockerfile/java:oracle-java7
MAINTAINER ServiceRocket Tools

ENV NODE_VERSION 0.10.35
ENV NPM_VERSION 2.1.16

RUN apt-get update && apt-get install -y \
    openssh-server \
    ca-certificates \
    curl

# Configure SSH as part of Jenkins slave requirement
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# Add user jenkins to the image
RUN adduser --quiet jenkins
RUN echo "jenkins:jenkins" | chpasswd

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV NVM_DIR /nvm
ENV PROFILE /etc/bash.bashrc
RUN mkdir $NVM_DIR \
  && chmod a+rw $NVM_DIR \
  && mkdir p /npm \
  && chmod a+rw /npm

RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.16.1/install.sh | sh \
  && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" \
  && nvm install $NODE_VERSION \
  && nvm use $NODE_VERSION \
  && nvm alias default $NODE_VERSION \
  && npm install -g npm@"$NPM_VERSION" \
  && cd /npm \
  && npm install --save lineman \
  && cd /npm/node_modules/lineman \
  && npm link

# Standard SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]