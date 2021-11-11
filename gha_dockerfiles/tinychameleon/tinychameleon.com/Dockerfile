FROM ubuntu:20.04 AS builder

RUN apt-get update && apt-get install -y curl

ARG version
RUN curl -Lo hugo_${version}.tar.gz https://github.com/gohugoio/hugo/releases/download/v${version}/hugo_extended_${version}_Linux-64bit.tar.gz
RUN tar -xzf hugo_${version}.tar.gz


FROM ubuntu:20.04
WORKDIR /workspace
COPY --from=builder /hugo /usr/local/bin/
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata && \
	rm -rf /var/lib/apt/lists/*
RUN ln -sf /usr/share/zoneinfo/Canada/Pacific /etc/localtime
ENTRYPOINT ["hugo"]
