FROM debian

RUN apt-get update && apt-get -y upgrade && \
    apt-get -y -o APT::Install-Recommend=false -o APT::Install-Suggests=false install \
    tcpdump netcat-traditional netcat-openbsd socat traceroute fio stress \ 
    iperf git ngrep nmap whois vim vim-common htop wget curl unzip screen openssh-client \
    net-tools hping3 dnsutils telnet less bash-completion \
    python-pip python3-virtualenv python-virtualenv python3 python3-pip \
    php7.0-cli php7.0-json php7.0-curl php-pear php-net-socket ftp procps man-db && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /var/log/* && \
    echo "source /usr/share/vim/vim80/defaults.vim\n\
let skip_defaults_vim = 1\n\
if has('mouse')\n\
    set mouse=r\n\
endif" >> /etc/vim/vimrc.local && \
    cp /etc/skel/.bashrc ~root/ && \
    useradd -u 1000 -d /home/user -m -s /bin/bash user
