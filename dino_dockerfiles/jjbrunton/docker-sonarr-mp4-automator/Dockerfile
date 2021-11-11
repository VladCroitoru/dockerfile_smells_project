FROM linuxserver/sonarr:develop

RUN \
  apt-get update && \
  apt-get install -y \
  ffmpeg \
  git \
  python-pip \
  openssl \
  python-dev \
  libffi-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev

RUN \
  python -m pip install --upgrade pip && \
  pip install requests && \
  pip install requests[security] && \
  pip install requests-cache && \
  pip install babelfish && \
  pip install 'guessit<2' && \
  pip install 'subliminal<2' && \
  pip install stevedore==1.19.1 && \
  pip install python-dateutil && \
  pip install qtfaststart && \
  git clone git://github.com/mdhiggins/sickbeard_mp4_automator.git /sickbeard_mp4_automator/ && \
  touch /sickbeard_mp4_automator/info.log && \
  chmod a+rwx -R /sickbeard_mp4_automator && \
  ln -s /downloads /data && \
  ln -s /config_mp4_automator/autoProcess.ini /sickbeard_mp4_automator/autoProcess.ini && \
  rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

VOLUME config_mp4_automator
