FROM ubuntu:14.04.3
MAINTAINER Mesosphere <support@mesosphere.io>

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -qqy \
        ca-certificates \
        curl \
        openssl \
        && \
    apt-get clean

RUN curl -o- https://raw.githubusercontent.com/karlkfi/resolveip/v1.0.2/install.sh | bash
RUN curl -o- https://raw.githubusercontent.com/karlkfi/intemp/v1.0.1/install.sh | bash
ENV TMPDIR /tmp

COPY ["entrypoint.sh", "kube-cagen.sh", "kube-certgen.sh", "kube-certgen-inner.sh", "kube-keygen.sh", "/usr/local/bin/"]

ENTRYPOINT ["entrypoint.sh"]
