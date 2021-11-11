FROM alpine:3.9
MAINTAINER Brint O'Hearn <brintly@gmail.com>

ENV DOCKER_COMPOSE_VERSION 1.24.0
ENV DOCKER_MACHINE_VERSION 0.16.0

# Python
ENV WORKON_HOME /home/user/.virtualenvs

# Ruby
ENV RBENV_VERSION 2.6.3

# All this stuff is done as root
RUN apk update && \
  apk upgrade && \
  apk add --no-cache build-base \
                     linux-headers \
                     readline-dev \
                     zlib-dev \
                     openssl \
                     openssl-dev \
                     vim \
                     zsh \
                     bash \
                     curl \
                     openssh-client \
                     ca-certificates \
                     file \
                     lftp \
                     python3 \
                     py3-yaml \
                     python3-dev \
                     musl-dev \
                     libffi-dev \
                     git && \
  adduser -D -s /bin/zsh user && \
  apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main --repository  http://dl-cdn.alpinelinux.org/alpine/edge/community docker go && \
  curl -L https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \
  chmod +x /usr/local/bin/docker-machine && \
  pip3 install -U pip virtualenv && \
  curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl > /usr/local/bin/kubectl && \
  chmod +x /usr/local/bin/kubectl && \
  rm -rf `find / -regex '.*\.py[co]' -or -name apk`

ENV PATH /home/user/.rbenv/bin:/home/user/.virtualenvs/user/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# All this stuff is done as a user
USER user
COPY .zshrc /home/user/.zshrc
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git /home/user/.oh-my-zsh && \
  mkdir -p $WORKON_HOME && \
  virtualenv /home/user/.virtualenvs/user && \
  source /home/user/.virtualenvs/user/bin/activate && \
  pip install -U docker-compose==${DOCKER_COMPOSE_VERSION} awscli azure-cli && \
  git clone https://github.com/rbenv/rbenv.git /home/user/.rbenv && \
  git clone https://github.com/sstephenson/ruby-build.git /home/user/.rbenv/plugins/ruby-build && \
  rbenv install $RBENV_VERSION

WORKDIR /home/user
CMD ["/bin/zsh"]
