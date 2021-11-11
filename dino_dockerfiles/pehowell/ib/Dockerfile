FROM pehowell/arch-dumbinit
LABEL maintainer="Paul Howell <paul.howell+docker@gmail.com>"

ENV TERM xterm

ENV TEMP_PKG "autoconf binutils fakeroot gcc make patch sudo git"
ENV NEEDED_PKG "gnu-netcat"

COPY start.sh /home/ib/start.sh
COPY jts.ini /home/ib/jts.ini

RUN pacman -Syu --noconfirm ${TEMP_PKG} ${NEEDED_PKG} && \
    groupadd -f wheel && \
    groupadd -f users && \
    useradd -G wheel -m ib && \
    chown -R ib:ib /home/ib && \
    chmod +x /home/ib/start.sh && \
    sed -i 's/^# \(.*\)NOPASSWD\(.*\)$/\1NOPASSWD\2/' /etc/sudoers

USER ib

RUN cd /tmp && \
    git clone https://aur.archlinux.org/ib-tws.git && \
    cd ib-tws && \
    makepkg -si --noconfirm --skipchecksums && \
    cd /tmp && \
    git clone https://aur.archlinux.org/ib-controller.git && \
    cd ib-controller && \
    makepkg -si --noconfirm && \
    cd /tmp && \
    git clone https://aur.archlinux.org/localepurge.git && \
    cd localepurge && \
    makepkg -si --noconfirm

USER root

RUN sed -i 's/^NEEDSCONFIGFIRST/#NEEDSCONFIGFIRST/' /etc/locale.nopurge && \
    localepurge -v && \
    mkdir -p /var/run/xvfb && \
    rm -rf /usr/share/man/* && \
    rm -rf /usr/share/doc/*

VOLUME /home/ib/config
WORKDIR /home/ib

EXPOSE 4001
CMD ["/bin/bash", "/home/ib/start.sh"]
