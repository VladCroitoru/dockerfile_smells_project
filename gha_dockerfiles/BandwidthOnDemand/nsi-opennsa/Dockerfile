# OpenNSA docker image suited for nsi-node deployment

FROM debian:stable-slim

MAINTAINER Hans Trompert <hans.trompert@surf.nl>


# -- Environment --
ENV OPENNSA_GIT_REPO https://github.com/NORDUnet/opennsa.git
ENV OPENNSA_VERSION 69d04b01fe239089a24f6bb2fb1e8b616a2a4923
ENV USER opennsa


# --- Base image ---
# Update and install dependencies
# pip to install twistar service-identity pyasn1
# pyasn1 and crypto is needed for ssh backends
RUN apt-get update
RUN apt-get install -y git-core python3 python3-twisted-bin python3-openssl python3-psycopg2 python3-pip python3-cryptography python3-dateutil python3-distutils
RUN pip3 install twistar service-identity pyasn1
# Debian bullseye has moved the /usr/bin/python symlink to a separate package
RUN apt-get install -y python-is-python3

# dependencies for workfloworchestrator backend (SURF)
RUN apt-get install -y python3-requests

# dependencies for paristaEOS4 backend (NRP Nautilus)
RUN apt-get install -y vim
RUN pip3 install paramiko


# -- User setup --
RUN adduser --disabled-password --gecos 'OpenNSA user' $USER


# -- Install OpenNSA --
USER $USER
WORKDIR /home/$USER

RUN git clone $OPENNSA_GIT_REPO && cd opennsa && git checkout $OPENNSA_VERSION

# -- Cleanup --
# With --squash this makes the image go from 476 to 164 mb
USER root
RUN apt-get remove -y python3-pip git
RUN apt-get -y clean
RUN apt-get -y autoclean
RUN apt-get -y autoremove


# -- Switch to OpenNSA directory --

USER $USER
WORKDIR /home/$USER/opennsa

ENV PYTHONPATH .

# -- Entrypoint --

EXPOSE 9080
EXPOSE 9443

# allow nsi-node custum backends to be loaded
ENV PYTHONPATH=/backends:$PYTHONPATH
ENTRYPOINT rm -f twistd.pid; twistd -ny opennsa.tac
