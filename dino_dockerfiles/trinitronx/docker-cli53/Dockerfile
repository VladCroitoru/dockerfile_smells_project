# vim:set ft=dockerfile:

# VERSION 0.7.1
# AUTHOR:         Alexander Turcic <alex@zeitgeist.se>
# AUTHOR:         James Cuzella <james.cuzella@lyraphase.com>
# DESCRIPTION:    cli53 in a Docker container
# TO_BUILD:       docker build --rm -t trinitronx/docker-cli53 .
# SOURCE:         https://github.com/trinitronx/docker-cli53

# Pull base image.
FROM debian:jessie
MAINTAINER James Cuzella "james.cuzella@lyraphase.com"

# Install dependencies.
RUN \
  echo 'deb http://http.debian.net/debian jessie-backports main' | tee /etc/apt/sources.list.d/jessie-backports.list && \
  apt-get update && \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get install -y git build-essential sudo acl && \
  sed -i -e '/^Defaults.*path/a\
Defaults\t!requiretty' \
    -e 's/^%sudo.*ALL$/%sudo    ALL=(ALL)    NOPASSWD: ALL/' \
    -e '/^%sudo.*ALL$/a %wheel   ALL=(ALL)    NOPASSWD: ALL' /etc/sudoers && \
  apt-get install -y -t jessie-backports golang && \
  export GOPATH=$HOME/go && mkdir -p $HOME/go && \
  export GO15VENDOREXPERIMENT=1 && \
  go get github.com/barnybug/cli53 && \
  cd $GOPATH/src/github.com/barnybug/cli53 && \
  make install && \
  mkdir -p ~/bin && \
  mv ~/go/bin/* /usr/local/bin/ && \
  rm -rf $HOME/go && \
  apt-get -y purge build-essential golang && \
  apt-get -y autoremove --purge && \
  rm -rf /var/lib/apt/lists/*

RUN \
  export uid=1000 gid=1000 && \
  groupadd --gid ${gid} user && \
  useradd --uid ${uid} --gid ${gid} --groups sudo --create-home user

USER user
WORKDIR /home/user

ENTRYPOINT ["/usr/local/bin/cli53"]
CMD ["-?"]
