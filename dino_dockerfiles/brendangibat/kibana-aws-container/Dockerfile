FROM debian:jessie

# add our user and group first to make sure their IDs get assigned consistently
RUN groupadd -r kibana && useradd -r -g kibana kibana

RUN apt-get update && apt-get -y install unzip curl

RUN apt-get update && apt-get -y install python
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

RUN apt-get update && apt-get install -y ca-certificates curl --no-install-recommends && rm -rf /var/lib/apt/lists/*

# grab gosu for easy step-down from root
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN arch="$(dpkg --print-architecture)" \
	&& set -x \
	&& curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \
	&& curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu

ENV KIBANA_VERSION 4.1.11
ENV KIBANA_SHA1 8c9cdc08e47cd6f0c4720122dd81ed8ed5b66a6d

RUN set -x \
	&& curl -fSL "https://github.com/brendangibat/kibana/releases/download/v4.1.11-aws/kibana-4.1.11-aws-linux-x64.tar.gz" -o kibana.tar.gz \
	&& echo "${KIBANA_SHA1}  kibana.tar.gz" | sha1sum -c - \
	&& mkdir -p /opt/kibana \
	&& tar -xz --strip-components=1 -C /opt/kibana -f kibana.tar.gz \
	&& rm kibana.tar.gz

ENV PATH /opt/kibana/bin:$PATH

COPY ./docker-entrypoint.sh /

EXPOSE 5601
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["kibana"]
