FROM nodesource/xenial:6.3.1


MAINTAINER Gabor Raz

RUN apt-get update
RUN apt-get update >/dev/null
RUN apt-get install -y git
RUN apt-get install -y curl


RUN apt-get update && apt-get install -y xvfb default-jre

# Install Firefox 45.4.0 (https://github.com/SeleniumHQ/selenium/blob/master/java/CHANGELOG#L33)
RUN curl -o /var/tmp/firefox-45.4.0esr.tar.bz2 https://ftp.mozilla.org/pub/firefox/releases/45.4.0esr/linux-x86_64/en-US/firefox-45.4.0esr.tar.bz2
RUN tar xvfj /var/tmp/firefox-45.4.0esr.tar.bz2
RUN ln -s /firefox/firefox-bin /usr/bin/firefox

RUN apt install chromium-browser


ADD xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser

RUN apt-get install -y build-essential
RUN apt-get install -y python
RUN apt-get install -y make
RUN apt-get install -y g++
RUN apt-get install -y libfontconfig
RUN apt-get install -y locales >/dev/null
RUN echo "en_US UTF-8" > /etc/locale.gen
RUN locale-gen en_US.UTF-8
RUN export LANG=en_US.UTF-8
RUN export LANGUAGE=en_US:en
RUN export LC_ALL=en_US.UTF-8
RUN npm install node-gyp -g
RUN curl https://install.meteor.com/ | sh
RUN apt-get install -y openssh-client
RUN echo 'PATH="/usr/local/node/bin:${PATH}"' >> /etc/bash.bashrc


