FROM bitnami/minideb:jessie
MAINTAINER Angus Lees <gus@inodes.org>

RUN install_packages git wget ca-certificates adduser
RUN adduser --home /home/user --disabled-password --gecos User user

RUN \
  wget https://storage.googleapis.com/kubernetes-release/release/v1.5.6/bin/linux/amd64/kubectl && \
  mv kubectl /usr/local/bin/ && \
  chmod +x /usr/local/bin/kubectl

COPY update-loop.sh /

USER user
WORKDIR /home/user
CMD ["/update-loop.sh"]
