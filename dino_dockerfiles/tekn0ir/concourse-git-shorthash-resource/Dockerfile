FROM alpine:3.6

RUN apk --update add \
  ca-certificates \
  bash \
  jq \
  git \
  openssh

# can't `git pull` unless we set these
RUN git config --global user.email "git@localhost" && \
    git config --global user.name "git"

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*

ENTRYPOINT ["bash", "-c"]
