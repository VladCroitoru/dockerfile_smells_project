# FROM python:2
FROM t3docs/python2-with-latex

# for apt-get
ARG DEBIAN_FRONTEND=noninteractive

# t3libreoffice:
ENV \
   OUR_IMAGE="t3docs/libreoffice-on-python2-with-latex" \
   OUR_IMAGE_SHORT=t3libreoffice

# BUILD
#    docker build -t t3docs/t3libreoffice .

LABEL \
   Maintainer="TYPO3 Documentation Team" \
   Description="\
This is LibreOffice on top of python:2 with LaTeX for TYPO3 \
Use it as a base image instead of python:2 \
if you desire to process OpenOffice manuals (manual.sxw)." \
   Vendor="t3docs" Version="1.0.0"

RUN \
   true "Create executable COMMENT as a workaround to allow commenting here" \
   && cp /bin/true /bin/COMMENT \
   \
   && apt-get update \
   && COMMENT "Install required packages" \
   && apt-get install -qy \
      libreoffice-base \
   \
   && COMMENT "Install convenience packages" \
   && apt-get install -qy --no-install-recommends \
      ncdu \
   \
   && COMMENT "Try extra cleaning besides /etc/apt/apt.conf.d/docker-clean" \
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/* \
   && rm -rf /tmp/* \
   ;
