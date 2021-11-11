FROM ubuntu:16.04
MAINTAINER Martin Hlavac <info@mhlavac.net>

RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install sudo git && \
    cd ~root && \
    git clone https://github.com/mhlavac/my-zsh.git && \
    cd my-zsh && \
    ./install.sh && \
    /bin/zsh --login -c "/bin/zsh ~/my-zsh/.zshrc" && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/cache/* && \
    rm -rf /var/lib/log/*

ENTRYPOINT ["/bin/zsh"]
