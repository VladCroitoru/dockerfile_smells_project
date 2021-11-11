FROM ubuntu:14.04
MAINTAINER Jason Gegere <jason@htmlgraphic.com>

# Install packages then remove cache package list information
RUN locale-gen en_US en_US.UTF-8 \
	&& apt-get update \
	&& apt-get -yq install build-essential \
	libssl-dev \
	libreadline-dev \
	libncurses5-dev \
	gcc \
	make \
	wget \
	openssh-client \
	redsocks \
	iptables \
	vim \
	lynx \
	iptables-persistent \
	git


COPY build.sh /build.sh
COPY run.c /usr/local/src/
RUN bash /build.sh \
	&& rm /build.sh

COPY app /app
RUN chmod 755 -R /app

RUN apt-get -y remove build-essential \
	&& apt-get clean \
	&& apt-get -y autoremove \
	&& rm -rf /var/lib/apt/lists/*


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


ENV PROXY_HOST=$PROXY_HOST \
	PROXY_PORT=$PROXY_PORT \
	LOCAL_IP=$LOCAL_IP \
	no_proxy=$NO_PROXY

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="VPN Docker" \
      org.label-schema.description="Docker container for SoftEther VPN" \
      org.label-schema.url="https://htmlgraphic.com" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/htmlgraphic/VPN" \
      org.label-schema.vendor="HTMLgraphic, LLC" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

WORKDIR /opt

ENTRYPOINT ["/entrypoint.sh"]

# Note that EXPOSE only works for inter-container links. It doesn't make ports accessible from the host. To expose port(s) to the host, at runtime, use the -p flag.
EXPOSE 500/udp 4500/udp 1701/tcp

CMD ["/usr/local/sbin/run"]
