FROM ubuntu
MAINTAINER Robert Clark <hyakuhei@gmail.com>
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
  python-dev \
  python-pip \
  git \
  libffi-dev \
  libssl-dev
WORKDIR /home
RUN git clone git://git.openstack.org/openstack/anchor
WORKDIR /home/anchor
RUN pip install .
RUN openssl req -out CA/root-ca.crt \
  -keyout CA/root-ca-unwrapped.key \
  -newkey rsa:4096 \
  -subj "/CN=Anchor Test CA" \
  -nodes \
  -x509 \
  -days 365
RUN chmod 0400 CA/root-ca-unwrapped.key
