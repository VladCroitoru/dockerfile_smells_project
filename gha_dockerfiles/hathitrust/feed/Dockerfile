FROM ghcr.io/hathitrust/perl_base:bullseye
LABEL org.opencontainers.image.source https://github.com/hathitrust/feed

RUN apt-get update && apt-get install -y \
    awscli \
    epubcheck \
    libclamav-client-perl \
    libswitch-perl \
    libtest-class-perl \
    libtest-mockobject-perl \
    libtest-most-perl \
    libtest-spec-perl \
    mariadb-client \
    netcat \
    rclone

ARG UNAME=ingest
ARG UID=1000
ARG GID=1000
ENV FEED_HOME=/usr/local/feed

RUN groupadd -g $GID -o $UNAME
RUN useradd -m -d $FEED_HOME -u $UID -g $GID -o -s /bin/bash $UNAME

USER $UID:$GID

RUN mkdir -p /tmp/stage/grin
RUN mkdir -p /tmp/prep/toingest /tmp/prep/failed /tmp/prep/ingested /tmp/prep/logs /tmp/prep/toingest/emma

WORKDIR $FEED_HOME

RUN mkdir $FEED_HOME/bin $FEED_HOME/src $FEED_HOME/.gnupg
RUN chown $UID:$GID $FEED_HOME/.gnupg
RUN chmod 700 $FEED_HOME/.gnupg
COPY ./src/validateCache.cpp $FEED_HOME/src/validateCache.cpp
RUN /usr/bin/g++ -o bin/validateCache src/validateCache.cpp -lxerces-c

COPY . $FEED_HOME
COPY ./etc/sample_namespace/TEST.pm $FEED_HOME/etc/namespaces/TEST.pm

ARG version=feed-development
ENV VERSION=$version
