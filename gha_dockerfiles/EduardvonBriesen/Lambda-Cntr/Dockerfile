# Example for a slim/fat container setup.

FROM rust:1.46.0 as cntr
RUN rustup target add x86_64-unknown-linux-musl

# Add docker-pid binary
RUN curl -sL https://github.com/Mic92/docker-pid/releases/download/1.0.0/docker-pid-linux-amd64 \
      > /usr/bin/docker-pid && \
      chmod 755 /usr/bin/docker-pid

# Add cntr binary
RUN wget https://github.com/Mic92/cntr/releases/download/1.5.1/cntr-src-1.5.1.tar.gz && \
      tar -xvf cntr-src-1.5.1.tar.gz
WORKDIR  /cntr-src-1.5.1
RUN cargo build --release --target=x86_64-unknown-linux-musl || true 
RUN strip target/x86_64-unknown-linux-musl/release/cntr -o /usr/bin/cntr

FROM alpine:edge

RUN echo 'https://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

RUN apk update && \
    apk add --no-cache \
    # build/code
    build-base git go bash bash-completion ncurses vim tmux jq \
    # network
    bind-tools iputils tcpdump curl nmap tcpflow iftop net-tools mtr netcat-openbsd bridge-utils iperf ngrep \
    # certificates
    ca-certificates openssl \
    # processes/io
    htop atop strace iotop sysstat ltrace ncdu logrotate hdparm pciutils psmisc tree pv \
    # kubernetes
    kubectl \
    containerd

WORKDIR /root/
COPY --from=cntr /usr/bin/cntr /usr/bin/cntr
COPY --from=cntr /usr/bin/docker-pid /usr/bin/docker-pid
ENTRYPOINT ["/usr/bin/cntr"]

# Credit to https://github.com/giantswarm/debug