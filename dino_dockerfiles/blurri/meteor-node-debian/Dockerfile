
FROM nodesource/jessie:0.12.7

MAINTAINER Gabor Raz
RUN apt-get update
RUN apt-get update >/dev/null
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN apt-get install -y git
RUN apt-get install -y curl

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


RUN apt-get update && apt-get install -y xvfb default-jre

# Install Firefox 45.4.0 (https://github.com/SeleniumHQ/selenium/blob/master/java/CHANGELOG#L33)
RUN curl -o /var/tmp/firefox-45.4.0esr.tar.bz2 https://ftp.mozilla.org/pub/firefox/releases/45.4.0esr/linux-x86_64/en-US/firefox-45.4.0esr.tar.bz2
RUN tar xvfj /var/tmp/firefox-45.4.0esr.tar.bz2
RUN ln -s /firefox/firefox-bin /usr/bin/firefox

RUN apt-get update
RUN apt-get install libxpm4 libxrender1 libgtk2.0-0 libnss3 libgconf-2-4
RUN apt-get install google-chrome-stable
RUN apt-get install xvfb gtk2-engines-pixbuf
RUN apt-get install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable
RUN apt-get install imagemagick x11-apps
RUN Xvfb -ac :99 -screen 0 1280x1024x16 &
RUN disown $1
RUN export DISPLAY=:99
