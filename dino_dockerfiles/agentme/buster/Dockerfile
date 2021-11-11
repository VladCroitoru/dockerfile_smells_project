FROM ubuntu:18.04

LABEL maintainer="agentme49@gmail.com"

ENV LANG C.UTF-8

# Add Tini
ARG TINI_VERSION=v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

RUN apt-get update && apt-get install -y \
    inotify-tools \
    python3 \
    python3-pip \
    unzip \
    wget

RUN mkdir /var/buster
WORKDIR /var/buster
COPY . .

RUN pip3 install -r requirements.txt

ARG USER=buster
ARG GROUP=buster
ARG PUID=1999
ARG PGID=1999

RUN groupadd -g $PGID $GROUP && useradd -u $PUID -g $GROUP $USER
RUN mkdir /var/static_ghost
RUN chown buster:buster /var/static_ghost
VOLUME /var/static_ghost

USER ${USER}:${GROUP}

ENV PYTHONUNBUFFERED TRUE
ENV GC_TIME_SECONDS 600

CMD [ "/var/buster/autobuster/main.py" ]
