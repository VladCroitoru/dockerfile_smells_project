ARG IONIC_VERSION=v3.20.0

FROM beevelop/ionic:${IONIC_VERSION}

RUN apt-get update && \
    apt-get install -y bzip2 python2.7 python-pip && \
    apt-get clean