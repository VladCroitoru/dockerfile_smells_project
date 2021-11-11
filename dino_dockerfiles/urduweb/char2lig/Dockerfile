FROM ubuntu
MAINTAINER Sawood Alam <ibnesayeed@gmail.com>

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get update && apt-get install -y libpango1.0-dev

ADD liggen /liggen
ADD fonts /root/.fonts

WORKDIR /liggen

# TODO: Add glyph import script and dependencies.
