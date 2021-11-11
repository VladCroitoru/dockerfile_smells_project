FROM ubuntu:16.04

ENV SCREEN_WIDTH 1360
ENV SCREEN_HEIGHT 1020
ENV SCREEN_DEPTH 24

# Install all of the package dependencies
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    bzip2 \
    ca-certificates \
    sudo \
    unzip \
    wget \
    curl \
    git-core \
    openssl \
    libssl-dev \
    python \
    python-dev \
    libevent1-dev \
    libffi-dev \
    x11-utils \
    x11vnc \
    xterm \
    xvfb \
    ttf-dejavu \
    fonts-ipafont-gothic \
    xfonts-100dpi \
    xfonts-75dpi \
    xfonts-cyrillic \
    xfonts-scalable \
    openbox \
    firefox \
    libasound2 \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && mkdir -p /opt/bin \
  && mkdir -p /root/.vnc \
  && x11vnc -storepasswd secret /root/.vnc/passwd \
  && curl -s -q "https://bootstrap.pypa.io/get-pip.py" | python

# Add normal user with passwordless sudo
RUN sudo useradd srvuser --shell /bin/bash --create-home \
  && sudo usermod -a -G sudo srvuser \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'srvuser:secret' | chpasswd

# install phantomjs
RUN sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
  && sudo tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/ \
  && sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

# install firefox 46
RUN sudo rm -rf /opt/firefox \
  && sudo rm -rf /usr/bin/firefox \
  && mkdir -p /opt/firefox/46.0.1 \
  && cd /opt/firefox/46.0.1 \
  && curl -sL "https://ftp.mozilla.org/pub/firefox/releases/46.0.1/linux-x86_64/en-US/firefox-46.0.1.tar.bz2" | tar jx --strip-components 1 \
  && sudo ln -s /opt/firefox/46.0.1/firefox /usr/bin/firefox

# install supervisord
RUN pip install supervisor \
  && mkdir -p /etc/supervisord/conf.d /var/log/supervisor

COPY supervisord.conf /etc/supervisord/supervisord.conf
COPY supervisor.*.conf /etc/supervisord/conf.d/

# expose vnc and supervisor control
EXPOSE 5900
EXPOSE 9001

CMD [ "/usr/local/bin/supervisord", "-c", "/etc/supervisord/supervisord.conf" ]
