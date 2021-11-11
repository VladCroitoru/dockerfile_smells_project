FROM python:latest

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VCS_URL
ARG VERSION
LABEL org.label-schema.build-date="2017-12-13T12:43:28Z" \
      org.label-schema.name="aws-gen" \
      org.label-schema.description="Machine for interacting with AWS infrastructure" \
      org.label-schema.url="https://github.com/chrisramsay/aws-gen" \
      org.label-schema.vcs-ref="c9a649add4b1cf46620de2ae370c30aa6862e5ae" \
      org.label-schema.vcs-url="git@github.com:chrisramsay/aws-gen.git" \
      org.label-schema.vendor="Chris Ramsay" \
      org.label-schema.version="0.14.3" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.maintainer="Chris Ramsay <chris@ramsay-family.net>"

RUN apt-get -y update && apt-get install -y \
  python \
  python-dev \
  python-pip \
  git \
  groff \
  vim

WORKDIR /srv
ADD requirements.txt /srv/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Shell bits
ADD files/bashrc /root/.bashrc
ADD build/VERSION /root/VERSION

