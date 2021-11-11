FROM ubuntu:14.04
MAINTAINER Yaniv E. 

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

RUN apt-mark hold initscripts udev plymouth mountall
RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

RUN sed -i "/^# deb.*multiverse/ s/^# //" /etc/apt/sources.list

RUN apt-get update

RUN apt-get install -y \
	supervisor \
        openssh-server \
	sudo \
        net-tools \
        lxde-core \
	lxde-icon-theme \
	x11vnc \
	xvfb \
	screen \
	openbox \
        nodejs \
	wget \
	htop \
	bmon \
	nano \
	lxterminal \
	locales \
	autocutsel \
	curl

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt-get -f install google-chrome-stable -y

RUN apt-get install -y --no-install-recommends \
        fonts-thai-tlwg \
        fonts-wqy-zenhei \
        language-pack-zh-hans \
        language-pack-zh-hans-base

RUN apt-get update && apt-get install -y \
	fcitx \
	fcitx-keyboard \
	fcitx-pinyin \
	fcitx-sunpinyin \
	leafpad

# Add the below 2 lines to the above apt-get install command to add Hangul and Anthy languages (korean ?)
# fcitx-anthy \
# fcitx-hangul \

RUN apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

ADD etc/apt/sources.list.d/tor.list /etc/apt/sources.list.d/tor.list

RUN gpg --keyserver keys.gnupg.net --recv A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89
RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -

RUN apt-get update
RUN apt-get install -y tor deb.torproject.org-keyring

ADD noVNC /noVNC
ADD startup.sh /
ADD supervisord.conf /
ADD root/.config/lxpanel/LXDE/panels/panel /root/.config/lxpanel/LXDE/panels/panel
ADD root/.config/openbox/lxde-rc.xml root/.config/openbox/lxde-rc.xml
ADD root/.config/pcmanfm/LXDE/desktop-items-0.conf root/.config/pcmanfm/LXDE/desktop-items-0.conf
ADD keyboard /etc/default/keyboard
ADD etc/xdg/lxsession/LXDE/autostart /etc/xdg/lxsession/LXDE/autostart
ADD bin/set_lang.sh /bin/set_lang.sh
ADD bin/launch_chrome.sh /bin/launch_chrome.sh
ADD etc/default/locale /etc/default/locale
ADD bin/export_locale.sh /bin/export_locale.sh
ADD root/.config/fcitx/profile /root/.config/fcitx/profile
RUN echo "LC_ALL=en_US.UTF-8\nLANG=en_US.UTF-8" >> /etc/environment
RUN dpkg-reconfigure locales
ADD etc/security/limits.conf /etc/security/limits.conf
ADD torrc /etc/tor/torrc
ADD root/chrome.desktop.tor /root/chrome.desktop.tor
ADD root/chrome.desktop.regular /root/chrome.desktop.regular
ADD rc.local /etc/rc.local

WORKDIR /

EXPOSE 6080

ENTRYPOINT ["/startup.sh"]
