FROM debian:stable-slim
LABEL maintainer "Lion Batata <lionbatata@gmail.com>"

COPY start.sh /start.sh
COPY locale.gen /etc/locale.gen

ENV DEBIAN_FRONTEND noninteractive
RUN echo "deb http://security.debian.org/debian-security jessie/updates main\n" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y \
  x11-utils \
  x11-apps \
  openssl \
  libcurl3 \
  libssl1.0.0 \
  libnss3-tools \
  apt-transport-https \
  ca-certificates \
  sudo \
  gnupg \
  hicolor-icon-theme \
  libgl1-mesa-dri \
  libgl1-mesa-glx \
  libpango1.0-0 \
  libpulse0 \
  libv4l-0 \
  fonts-symbola \
  xauth \
  locales \
  python2.7 \
  python3 \
  python-openssl \
  zenity \
  libgtk2.0-0 \
  firefox-esr \
  firefox-esr-l10n-pt-br \
  --no-install-recommends \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && groupadd -g 1000 -r bank \
  && useradd -u 1000 -r -g bank -G audio,video bank \
  && mkdir -p /home/bank/Downloads \
  && chown -R bank:bank /home/bank \
  && echo "bank ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
  && chmod 0440 /etc/sudoers \
  && passwd -d root \
  && chmod 755 /start.sh \
  && locale-gen pt_BR.UTF-8 \
  && dpkg-reconfigure locales \
  && update-locale LANG=pt_BR.UTF-8 \
  && ln -s /start.sh /usr/local/bin/start.sh 

ADD https://cloud.gastecnologia.com.br/bb/downloads/ws/warsaw_setup64.deb /warsaw_setup64.deb
COPY local.conf /etc/fonts/local.conf

USER bank
ENV HOME /home/bank

ENTRYPOINT ["start.sh"]
