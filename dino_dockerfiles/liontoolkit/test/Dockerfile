FROM debian:latest

RUN	   apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
			build-essential \
			git \
			wget \
			python \
			ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

RUN mkdir /workspace
VOLUME /workspace

EXPOSE 8181

CMD ["bash"]
