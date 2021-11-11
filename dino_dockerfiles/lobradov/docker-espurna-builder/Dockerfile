FROM        bitnami/minideb:jessie
MAINTAINER  Lazar Obradovic <laz.obradovic@gmail.com>

ENV         PLATFORMIO_LIBDEPS_DIR="/usr/lib/platformio"
ENV         PLATFORMIO_HOME_DIR="/usr/share/platformio"



# This trashes caching, I know.
# But, we need requirements.txt for next step, and next step needs to be
# single-line, so... size vs speed.
ADD \
  https://raw.githubusercontent.com/xoseperez/espurna/dev/code/platformio.ini \
  https://raw.githubusercontent.com/xoseperez/espurna/dev/code/requirements.txt \
  https://raw.githubusercontent.com/xoseperez/espurna/dev/code/gulpfile.js \
  https://raw.githubusercontent.com/xoseperez/espurna/dev/code/package.json \
  https://raw.githubusercontent.com/xoseperez/espurna/dev/code/package-lock.json \
  /usr/src/

ADD \
    empty.ino \
    build-deps.py \
    entrypoint.sh /

RUN \
    install_packages \
      python \
      python-pip \
      python-setuptools \
      python-dev \
      python-wheel \
      git \
      curl \
      build-essential \
      gnupg \
      gcc &&\
    pip2 install -U pip &&\
    curl -sL https://deb.nodesource.com/setup_9.x | bash - &&\
    install_packages \
      nodejs &&\
    pip install -r /usr/src/requirements.txt &&\
    apt-get autoremove -yq \
      gcc \
      python-dev \
      python-wheel &&\
    apt-get autoclean &&\
	  rm -rf /var/lib/apt/lists/*

RUN \
    pip install -U platformio &&\
    pio upgrade --dev &&\
    /build-deps.py

VOLUME ["/usr/src/espurna"]

ENTRYPOINT ["/entrypoint.sh"]
