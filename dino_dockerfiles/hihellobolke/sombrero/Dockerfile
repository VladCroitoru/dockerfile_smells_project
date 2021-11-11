FROM hihellobolke/sombrero:base
LABEL maintainer="hihellobolke@gmail.com"

RUN dnf install -y bind-utils net-tools iputils traceroute whois \
        openssh-clients gnupg openssl kmod gcc-c++ procps-ng lsof cmake redhat-rpm-config python3-devel
RUN dnf -y clean all \
    && rm -rf /tmp/*

COPY files /files
RUN cat /files/bashrc >> /root/.bashrc \
    && cat /files/profile >> /etc/profile

ENTRYPOINT ["bash"]
CMD ["--login"]
