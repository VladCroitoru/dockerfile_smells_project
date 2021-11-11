FROM scottweston/java-oracle:7
MAINTAINER Scott Weston <scott@hronboard.me>

ENV ANT_VERSION 1.9.5

RUN set -x \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \
    build-essential \
    libssl-dev \
    netcat-openbsd \
    mercurial \
    mercurial-common \
    zlib1g-dev \
  && wget -q http://www.us.apache.org/dist//ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz \
  && tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz \
  && mv apache-ant-${ANT_VERSION} /opt/ant \
  && rm apache-ant-${ANT_VERSION}-bin.tar.gz

ENV ANT_HOME /opt/ant
ENV PATH ${PATH}:/opt/ant/bin

RUN mkdir -p /code
VOLUME [ "/code" ]
WORKDIR /code

ENTRYPOINT ["ant"]
CMD ["--help"]
