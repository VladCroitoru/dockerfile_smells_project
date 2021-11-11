FROM ubuntu:16.04
MAINTAINER Matthew Baltrusitis <matthew@baltrusitis.com>

ENV DEBIAN_FRONTEND="noninteractive"
ENV HOME /opt/sabnzbd
ENV DOWNLOADS_PATH $HOME/Downloads/complete

RUN apt-get -qy update && \
    apt-get install -qy software-properties-common && \
		add-apt-repository multiverse && \
		apt-get -qy update && \
		apt-get install -qy \
      ffmpeg \
      sabnzbdplus \
      sabnzbdplus-theme-classic \
      sabnzbdplus-theme-mobile \
      sabnzbdplus-theme-plush \
      p7zip \
      par2 \
      python-yenc \
      python-openssl \
      python-pip \
			vim \
      unrar \
      unzip \
      unrar && \
    pip install setuptools \
      requests \
      requests[security] \
      requests-cache \
      babelfish \
      guessit\<2 \
      subliminal\<2 \
      deluge-client \
      qtfaststart && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

VOLUME ["${HOME}", "${DOWNLOADS_PATH}"]
EXPOSE 8080 9090

CMD ["sabnzbdplus", "-b", "0", "-s", "0.0.0.0:8080", "--https", "9090"]

