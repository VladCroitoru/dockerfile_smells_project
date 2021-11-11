FROM caperneoignis/moodle-php-apache:7.1

USER root

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
#//fixes issue with chrome and potentially speeds up system. 
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
#===================
# Timezone settings
# Possible alternative: https://github.com/docker/docker/issues/3359#issuecomment-32150214
#===================
ENV TZ "US/Eastern"
RUN echo "${TZ}" > /etc/timezone \
  && dpkg-reconfigure --frontend noninteractive tzdata

  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >> /etc/apt/sources.list.d/jessie-backports.list
#==========================
# install java for selenium
#==========================
RUN apt-get update -qqy \
  && apt-get install -qqy -t jessie-backports \
  openjdk-8-jre-headless \
  ca-certificates-java  

#========================
# Miscellaneous packages
# Includes minimal runtime used for executing non GUI Java programs
#========================
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    bzip2 \
    sudo \
    unzip \
    wget \
	tzdata \
	debian-keyring \
  && rm -rf /var/lib/apt/lists/* 

RUN sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security

#==============
# VNC, java and Xvfb 
#==============
RUN apt-get update -qqy \
  && apt-get -qqy install \
    locales \
    xvfb \
  && rm -rf /var/lib/apt/lists/*

#==========
# Selenium
#==========
RUN  mkdir -p /opt/selenium \
  && wget --no-verbose \
  https://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.1.jar \
  -O /opt/selenium/selenium-server-standalone.jar
  
COPY config.json /opt/selenium/config.json
#============================
# Some configuration options
#============================
ENV SCREEN_WIDTH 1360
ENV SCREEN_HEIGHT 1020
ENV SCREEN_DEPTH 24
ENV DISPLAY :99.0


#=========
# Firefox
#=========
  
ENV FIREFOX_VERSION 47.0.1
RUN apt-get update \
  && apt-get -qq --force-yes --no-install-recommends install firefox-esr \
  && rm -rf /var/lib/apt/lists/* \
  && wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2 \
  #&& apt-get -y purge firefox-esr \
  && rm -rf /opt/firefox \
  && tar -C /opt -xjf /tmp/firefox.tar.bz2 \
  && rm /tmp/firefox.tar.bz2 \
  && ln -fs /opt/firefox/firefox /usr/bin/firefox

 
#============
# GeckoDriver
#============
ENV GECKODRIVER_VERSION 0.10.0
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
  && rm -rf /opt/geckodriver \
  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \
  && chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \
  && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver \
  && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/wires

  
#==============================
# Scripts to run Selenium Node
#==============================
COPY entry_point.sh /opt/bin/entry_point.sh
RUN chmod +x /opt/bin/entry_point.sh

#overwrite old configs with custom configs with export Document root
COPY configs/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY configs/apache2.conf /etc/apache2/apache2.conf

#set work directory to be the root system, since CI/CD like gitlab run from custom directory in build image. 
WORKDIR /

#first two commands are set in the above image, the 3rd is the selenium specific one.
ENTRYPOINT [ "/opt/bin/entry_point.sh", "docker-php-entrypoint"]



CMD ["apache2-foreground"]