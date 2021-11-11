FROM nginx:latest

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

# RUN apt-get update \
#	&& DEBIAN_FRONTEND=noninteractive \
#	apt-get install -y \
#	openssl \
#	&& rm -rf /var/lib/apt/lists/*

COPY copyables /

ENV CONFD_VERSION 0.10.0

ADD https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 /opt/confd/confd

RUN chmod +x /opt/confd/confd /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 443

CMD ["/opt/confd/confd"]
