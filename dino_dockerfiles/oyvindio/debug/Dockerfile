FROM debian:buster
RUN apt-get update && \
        apt-get install --no-install-recommends -y \
        curl \
        vim \
        nmap \
        traceroute \
        tcptraceroute \
        strace \
        dnsutils \
        socat \
        netcat \
        mtr-tiny \
        iperf \
        tcpdump \
        telnet \
        openssl \
        ca-certificates \
        && \
apt-get clean -y && \
apt-get autoclean -y && \
apt-get autoremove -y && \
        curl -Lo /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.17.0/bin/linux/amd64/kubectl && \
        curl -Lo /tmp/kubectl.sha256 https://storage.googleapis.com/kubernetes-release/release/v1.17.0/bin/linux/amd64/kubectl.sha256 && \
        echo "$(cat /tmp/kubectl.sha256)  /usr/local/bin/kubectl" | sha256sum -c -  && \
        rm -f /tmp/kubectl.sha256 && \
        chmod a+x /usr/local/bin/kubectl
ADD run-tests /run-tests
ENTRYPOINT ["tail", "-f", "/dev/null"]
