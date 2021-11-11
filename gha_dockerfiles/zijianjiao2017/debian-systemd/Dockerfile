FROM debian:bullseye
MAINTAINER ImFatF1sh <imfatf1sh@protonmail.com>
ENV container=docker LANG=C.UTF-8
RUN export DEBIAN_FRONTEND=noninteractive && \
    export LC_ALL=C && \
    mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo 'deb http://mirrors.bfsu.edu.cn/debian/ bullseye main contrib non-free' > /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.bfsu.edu.cn/debian/ bullseye main contrib non-free' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.bfsu.edu.cn/debian/ bullseye-updates main contrib non-free' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.bfsu.edu.cn/debian/ bullseye-updates main contrib non-free' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.bfsu.edu.cn/debian/ bullseye-backports main contrib non-free' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.bfsu.edu.cn/debian/ bullseye-backports main contrib non-free' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.bfsu.edu.cn/debian-security bullseye-security main contrib non-free' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.bfsu.edu.cn/debian-security bullseye-security main contrib non-free' >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests apt-utils && \
    apt-get install -y --no-install-recommends --no-install-suggests ca-certificates apt-transport-https && \
    sed -i 's/http:\/\//https:\/\//g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests software-properties-common && \
    apt-get upgrade -y --no-install-recommends --no-install-suggests && \
    # yes | unminimize && \
    apt-get install --no-install-recommends --no-install-suggests -y \
    dialog ccache curl unzip rsync build-essential systemd-cron dbus libncurses5-dev gnupg \
    squashfs-tools sudo rsyslog wget git libssl-dev libncurses5 lib32z1-dev zip git-core \
    bash vim libc6-dev-i386 python3-apt lib32ncurses5-dev libwxgtk3.0-gtk3-dev nano \
    lib32readline-dev openssh-client systemd lsb-release gnupg2 expect tmux ncdu p7zip-full \
    unrar neofetch tar cpio gzip htop coreutils iputils-ping bash-completion net-tools \
    apt-file command-not-found less man-db clang zlib1g-dev file gdebi aria2 bind9-dnsutils \
    systemd-sysv && \
    useradd -m -s /bin/bash -u 1000 debian && \
    usermod -aG sudo debian && \
    cp -avf /etc/environment /etc/environment.original && \
    rm -f ~/.bash_aliases ~/.gitconfig ~/.gitignore_global && \
    su debian -c 'curl https://mirror.ghproxy.com/https://gist.githubusercontent.com/zijianjiao2017/b7f70c36dbcc44a2668760f8384eb0b1/raw/5941e56798ea15b064a5bb4812436acba58c0d5f/.bash_aliases -o ~/.bash_aliases' && \
    su debian -c 'curl https://mirror.ghproxy.com/https://gist.githubusercontent.com/zijianjiao2017/a9e31d00eaf90950204227d99fa74c29/raw/fcc7fc88cc07cdd116d2a0aeab0373140ae9ef07/.gitconfig -o ~/.gitconfig' && \
    su debian -c 'curl https://mirror.ghproxy.com/https://gist.githubusercontent.com/zijianjiao2017/1c703c8d13a8249aef2b3b6aa575d50f/raw/7396d62a63a532278222c274ba0a453019248c6f/.gitignore_global -o ~/.gitignore_global' && \
    su debian -c 'mkdir -p ~/.bin/auto-ssh-agent' && \
    su debian -c 'git clone -b stable --single-branch --depth=1 --no-tags https://mirrors4.bfsu.edu.cn/git/git-repo ~/.bin/git-repo' && \
    su debian -c 'curl https://mirror.ghproxy.com/https://gist.githubusercontent.com/zijianjiao2017/a3edae819abbe8a55fd0070a7900fe88/raw/973cf35f76740e20e655e61a7445090ab7995404/ensure-ssh-agent -o ~/.bin/auto-ssh-agent/ensure-ssh-agent' && \
    su debian -c 'mkdir -p ~/.ssh' && \
    su debian -c 'chmod 700 ~/.ssh' && \
    su debian -c 'curl https://mirror.ghproxy.com/https://gist.githubusercontent.com/zijianjiao2017/bb3e704cf9538db4e50139e7b7dbbe49/raw/a6d2d71c28649ba33ce26c7853c3487a6fcd9735/id_rsa.pub -o ~/.ssh/id_rsa.pub' && \
    su debian -c 'chmod 644 ~/.ssh/id_rsa.pub' && \
    su debian -c 'curl https://mirror.ghproxy.com/https://gist.githubusercontent.com/zijianjiao2017/1d1ba498bd9d070098452a9964b1807d/raw/0c6382693cad32377700572cc6a23fbdb3c53f57/public_key.pub -o ~/public_key.pub' && \
    su debian -c 'gpg2 --import ~/public_key.pub' && \
    su debian -c 'rm -f ~/public_key.pub' && \
    su debian -c 'mkdir -p ~/.config/htop' && \
    su debian -c 'curl https://mirror.ghproxy.com/https://gist.githubusercontent.com/zijianjiao2017/f0937b1432a1e529f6d0d02e62589672/raw/8fa271d878de9f6ff6e7331f55bd4e6170104bb1/htoprc -o ~/.config/htop/htoprc' && \
    ln -s /mnt/workspace /workspace && \
    ln -s /mnt/workspace /home/debian/Workspace && \
    rm -f /etc/apt/apt.conf.d/docker-gzip-indexes && \
    apt-file update && \
    apt-get autopurge -y && \
    (dpkg -l | grep '^rc' | awk '{print $2}' | xargs apt-get -y purge) && \
    apt-get clean && \
    apt-get autoclean all -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    sed -i 's/^\(module(load="imklog")\)/#\1/' /etc/rsyslog.conf && \
    find /etc/systemd/system \
    /lib/systemd/system \
    -path '*.wants/*' \
    -not -name '*dbus*' \
    -not -name '*journald*' \
    -not -name '*systemd-tmpfiles*' \
    -not -name '*systemd-user-sessions*' \
    -exec rm \{} \; && \
    systemctl set-default multi-user.target && \
    systemctl mask dev-hugepages.mount sys-fs-fuse-connections.mount
STOPSIGNAL SIGRTMIN+3
CMD ["/sbin/init", "--log-target=journal"]
