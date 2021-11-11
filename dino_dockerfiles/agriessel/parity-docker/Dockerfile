FROM ubuntu:14.04

ENV PARITY_DEB_URL=https://github.com/agriessel/parity/releases/download/v1.5.0/parity_1.5.0_amd64.deb
# install tools and dependencies
RUN apt-get update
RUN apt-get install -y curl

RUN curl -L $PARITY_DEB_URL  > /tmp/parity.deb
RUN dpkg -i /tmp/parity.deb
RUN rm /tmp/parity.deb
