FROM teenooch/golang-plus:latest

LABEL maintainer="Martin Purmann <tinu.public@generalmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      git \
      gconf2 \
      gconf-service \
      gvfs-bin \
      fakeroot \
      libasound2 \
      libcap2 \
      libgconf-2-4 \
      libgtk2.0-0 \
      libnotify4 \
      libnss3 \
      libx11-xcb1 \
      libxkbfile1 \
      libxss1 \
      libxtst6 \
      python \
      xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -d /home/atom -m atom

#-----------------------------------------------------------------

ENV ATOM_VERSION v1.22.0
ENV ATOM_DOWNLOAD_URL https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom-amd64.deb

RUN curl -L "$ATOM_DOWNLOAD_URL" -o atom.deb \
  && dpkg -i atom.deb \
  && rm -f atom.deb \
  && rm -rf /var/lib/apt/lists/*

#-----------------------------------------------------------------

USER atom

RUN git clone --depth 1 https://github.com/teenooCH/dotfiles.git \
  && cp dotfiles/docker_env/bashrc_alias $HOME/.bashrc_alias; cp dotfiles/docker_env/bashrc $HOME/.bashrc \
  && ( cd dotfiles/atom; ./setupAtom.sh atom ) \
  && rm -rf dotfiles


CMD ["/usr/bin/atom","-f"]
