FROM buildpack-deps:focal

RUN sed -i '/^deb/ N; s/# deb-src/deb-src/' /etc/apt/sources.list && \
    \
    yes | env DEBIAN_FRONTEND=noninteractive unminimize && \
    \
    env DEBIAN_FRONTEND=noninteractive apt-get install -y \
    lsof parallel debootstrap tmux apt-file nmap busybox mlocate iproute2 tree \
    vim man-db strace sudo socat redir htop jq tsocks rsync dropbear-initramfs \
    openssh-server git pv elinks kpartx fakechroot python-all dnsmasq graphviz \
    fakeroot python3-all python3-doc nginx-extras                              \
    build-essential cloc awscli bash-completion lshw xinetd                    \
    postgis postgis-doc postgresql-12-pgrouting postgresql-12-pgrouting-doc    \
    dos2unix pgformatter erlang-base dnsutils telnet graphicsmagick            \
    mc iotop pandoc texlive texlive-latex-extra manpages-dev manpages          \
    glibc-doc autossh valgrind lvm2 ruby-dev python3-pygments binutils-doc     \
    pypy nodejs sox libsox-fmt-all lua5.2 lua5.2-doc python3-sphinx            \
    python3-flake8 pastebinit clang clang-10-doc iputils-ping debhelper pigz   \
    supervisor golang autotools-dev nftables debian-archive-keyring            \
    screen gdb-doc netcat-openbsd sloccount dh-systemd python3-dev pbuilder    \
    bsdgames gdb ddd ddd-doc rkt ghc zsh nginx-doc libsystemd-dev psmisc info  \
    ipython3 youtube-dl python3-matplotlib cowsay gcc-doc doc-rfc parted       \
    gdebi aptitude mysql-client mdadm musl-tools units sqlite grub2            \
    python3-yaml pgcli lynx iodine bc mencoder cmake git-buildpackage zip      \
    unzip mtr python3-pandas python3-scipy jupyter pax biber stow upx-ucl      \
    python-pandas-doc cython3 cowbuilder wait-for-it ctags gpgv2 moreutils     \
    pdftk-java libsox-dev unrar less openvpn latexmk texlive-lang-european     \
    software-properties-common shellcheck protobuf-compiler tzdata rtorrent    \
    spatialite-bin cloud-guest-utils qemu-system-x86 libsqlite3-mod-spatialite \
    cdebootstrap cdebootstrap-static docker.io linux-image-generic tcpdump     \
    syslinux pxelinux udev cryptsetup entr lz4 binwalk gdal-bin ethtool hdparm \
    pktools memtest86+ sdparm ntp ntpdate geotiff-bin neovim wireguard      && \
    \
    systemctl disable \
        NetworkManager.service \
        apparmor.service \
        apt-daily-upgrade.timer apt-daily.timer \
        avahi-daemon.service avahi-daemon.socket \
        containerd.service \
        dnsmasq.service \
        epmd.service epmd.socket \
        nginx.service \
        openvpn.service \
        postgresql.service \
        snapd.socket \
        supervisor.service \
        ubuntu-fan.service \
        unattended-upgrades.service \
        xinetd.service && \
    \
    curl -L recs.pl > /usr/local/bin/recs && chmod a+x /usr/local/bin/recs && \
    curl -o /etc/dropbear-initramfs/authorized_keys \
        https://github.com/motiejus.keys && \
    chmod 600 /etc/dropbear-initramfs/authorized_keys && \
    \
    git clone \
        https://github.com/motiejus/dotfiles \
        /root/.dotfiles && \
    stow -d /root/.dotfiles ctags tmux vim && \
    \
    apt-file update

COPY overlay/ /

RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    \
    sed -i '$a CRYPTSETUP=y' /etc/cryptsetup-initramfs/conf-hook && \
    ln /boot/vmlinuz-* /var/lib/tftpboot/pxelinux/vmlinuz && \
    ln /boot/initrd.img-* /var/lib/tftpboot/pxelinux/initrd.img && \
    ln /boot/memtest86+.bin /var/lib/tftpboot/pxelinux/memtest && \
    ln /usr/lib/syslinux/modules/bios/ldlinux.c32 \
         /usr/lib/syslinux/modules/bios/vesamenu.c32 \
         /usr/lib/syslinux/modules/bios/libcom32.c32 \
         /usr/lib/syslinux/modules/bios/libutil.c32 \
         /usr/lib/PXELINUX/pxelinux.0 \
      /var/lib/tftpboot/pxelinux/ && \
    update-initramfs -v -k all -u && \
    \
    updatedb
