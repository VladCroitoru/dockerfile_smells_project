FROM alpine:latest

WORKDIR /root

RUN apk update && \
  apk add \
    htop \
    tcpdump \
    nload \
    lsof \
    strace \
    git \
    tmux \
    file \
    vim \
    curl && \
  curl -s https://raw.githubusercontent.com/invisiblethreat/dotfiles/master/tmux.conf >/root/.tmux.conf

CMD ["/usr/bin/tmux", "-2"]
