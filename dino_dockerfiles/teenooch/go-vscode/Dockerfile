FROM teenooch/golang-plus:latest

LABEL maintainer="Martin Purmann <tinu.public@generalmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      libasound2 \
      libgconf-2-4 \
      libgnome-keyring-dev \
      libgtk2.0-0 \
      libnotify4 \
      libnss3 \
      libpci3 \
      libsecret-1-0 \
      libxss1 \
      libxtst6 \
      libxkbfile1 \
      libx11-xcb1 \
      unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -d /home/vscode -m vscode

ENV VSC_DOWNLOAD_URL https://go.microsoft.com/fwlink/?LinkID=760868

RUN curl -L "$VSC_DOWNLOAD_URL" -o vsc.deb \
  && dpkg -i vsc.deb \
  && rm -f vsc.deb \
  && rm -rf /var/lib/apt/lists/*

USER vscode

RUN git clone --depth 1 https://github.com/teenooCH/dotfiles.git \
  && cp dotfiles/docker_env/bashrc_alias $HOME/.bashrc_alias; cp dotfiles/docker_env/bashrc $HOME/.bashrc \
  && ( cd dotfiles/vscode; ./setupVSCode.sh ) \
  && rm -rf dotfiles

CMD  ["/usr/bin/code","--wait","--verbose"]
