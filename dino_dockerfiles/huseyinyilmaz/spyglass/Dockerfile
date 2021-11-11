#============================ build stage ============================
FROM fpco/stack-build:lts-13.22 as builder
RUN apt update; apt install build-essential
# Add default configuration.
RUN mkdir -p /etc/spyglass
ADD configuration/config.yaml /etc/spyglass/config.yaml
RUN mkdir /opt/build
WORKDIR /opt/build
ADD . .
RUN stack build --system-ghc
#============================= run stage =============================
FROM ubuntu:18.04
RUN mkdir -p /opt/spyglass
ARG BINARY_PATH
WORKDIR /opt/spyglass
RUN apt-get update && apt-get install -y \
  ca-certificates \
  build-essential \
  libgmp-dev
COPY --from=builder /opt/build/.stack-work/install/x86_64-linux/lts-13.22/8.6.5/bin .
# copy configuration
COPY configuration/config.yaml /etc/spyglas/config.yaml
# COPY static /opt/spyglass/static
# COPY config /opt/spyglass/config
CMD ["/opt/spyglass/spyglass"]
