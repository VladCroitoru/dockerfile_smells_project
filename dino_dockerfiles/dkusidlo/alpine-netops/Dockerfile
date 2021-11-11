FROM alpine

ENTRYPOINT ["/entrypoint.sh"]

RUN apk --update add \
    fping \
    htop \
    openssh \
    nmap \
    nmap-scripts \
    net-tools \
    iproute2 \
    curl \
    tcpdump \
    bind-tools \
    jq \
    nmap-ncat \
    iperf3 && \
    sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && rm -rf /var/cache/apk/*


COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
