# vim: syntax=dockerfile
# version: 0.0.1
#
# Pre-compiled binaries with Parity - fast, light, and robust Ethereum implementation.

FROM debian:stretch
LABEL maintainer="VS <github@roundside.com>"
SHELL ["/bin/bash", "-c"]

RUN DEBIAN_FRONTEND=noninteractive apt-get update -yqq && \
    apt-get upgrade -yqq && \
    apt-get install sudo wget curl ca-certificates lsb-release --no-install-recommends -yqq && \
    bash <(curl https://get.parity.io -kL)

ENTRYPOINT ["/usr/bin/parity"]
