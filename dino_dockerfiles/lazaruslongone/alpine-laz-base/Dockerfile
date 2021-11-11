FROM lazaruslongone/alpine-openrc-base:latest
MAINTAINER lazaruslongone

# non-root user
RUN adduser -G abuild -g "alpiner" -s /bin/bash -D alpiner

# add longlivelaz repo
ENV longlivelaz_repo_pubkey="lazaruslongone@gmail.com-573603ee.rsa.pub"

# install sudo and add alpiner with passwordless sudo
RUN apk update && apk add sudo && \
    echo "alpiner ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install the packages we want included by default
RUN apk update && \
  apk add openssh bash \
  vim rsync git curl coreutils \
  gawk sed grep bc go

# add longlivelaz repo
RUN curl -s https://apkrepo.longlivelaz.xyz/repo/${longlivelaz_repo_pubkey} \
    > /etc/apk/keys/${longlivelaz_repo_pubkey} && \
    echo "http://apkrepo.longlivelaz.xyz/repo" >> \
    /etc/apk/repositories

# setup alpiner user environment
USER alpiner
RUN echo "source /etc/profile" > /home/alpiner/.bashrc
WORKDIR /home/alpiner

ENTRYPOINT ["/bin/bash"]
