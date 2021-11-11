From ubuntu:20.04

RUN echo locales locales/default_environment_locale select en_US.UTF-8 | debconf-set-selections \
&& echo locales locales/locales_to_be_generated select "en_US.UTF-8 UTF-8" | debconf-set-selections \
&& sed -i -r 's!(deb|deb-src) \S+!\1 mirror://mirrors.ubuntu.com/mirrors.txt!' /etc/apt/sources.list \
&& apt update && DEBIAN_FRONTEND=noninteractive apt install --no-install-recommends -y \
    locales \
    git \
    vim-tiny \
    less \
    tmux \
    pwgen \
    openssh-client \
    openbox \
    tint2 \
    xfonts-base \
    tightvncserver \
    firefox \
    xrdp \
    pcmanfm \
    lxterminal \
    meld \
    scite \
    keepassx \
    dbus-x11 \
    ibus-anthy \
    ibus-gtk \
    ibus-gtk3 \
    fonts-ipaexfont \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

ADD xrdp.ini /etc/xrdp/xrdp.ini
ADD run.sh /run.sh
RUN chmod +x /run.sh
RUN useradd -s /bin/bash -m docker

EXPOSE 3389
CMD ["/run.sh"]
