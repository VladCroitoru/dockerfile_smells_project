FROM fike/debian:jessie.en_US

MAINTAINER Fernando Ike <fike@midstorm.org>

ENV DEBIAN_FRONTEND noninteractive

ENV DISPLAY :99

RUN sed -i 's/jessie\ main/jessie\ main\ contrib\ non-free/g' /etc/apt/sources.list && \
      sed -i 's/jessie\-updates\ main/jessie\-updates\ main\ contrib\ non-free/g' \
      /etc/apt/sources.list && \
      echo deb http://mozilla.debian.net/ jessie-backports \
        iceweasel-release >> /etc/apt/sources.list.d/mozilla.list

RUN apt-get update -y && apt-get upgrade -y && \
      apt-get install --no-install-recommends curl -qq

RUN curl -s -O http://mozilla.debian.net/pkg-mozilla-archive-keyring_1.1_all.deb \
      && dpkg -i pkg-mozilla-archive-keyring_1.1_all.deb && rm *.deb && \
      apt-get update -qq

RUN apt-get install --no-install-recommends xfonts-100dpi \
      xfonts-75dpi xfonts-scalable xfonts-cyrillic xvfb python-pip -qq && \
      apt-get install -t jessie-backports --no-install-recommends iceweasel \
      ca-certificates -qq 

RUN pip install selenium

WORKDIR /opt/annabe

RUN curl -s --location -O $(curl -s --location https://addons.mozilla.org/en-US/firefox/addon/har-export-trigger/versions/ | \
      sed -n -e 's/.*\(https\:.*har_export_trigger.*\.xpi\).*/\1/p'| head -n1) 

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD annabe /usr/local/bin/

ADD firefox_navigate.py /opt/annabe/

RUN chmod +x /opt/annabe/firefox_navigate.py /usr/local/bin/annabe
