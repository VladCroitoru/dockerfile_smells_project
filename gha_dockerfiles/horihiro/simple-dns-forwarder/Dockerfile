# Using multistage docker file to separate build and runtime containers separate
# For security and reliability use sha256 checksums for pinning, tags are mutable
# Add comment for docker tag for future reference gcc:10
FROM gcc:10.3.0-buster as build
# Install specific version
ARG VERSION="2.86"
# Get signing key
RUN gpg --keyserver hkp://keyring.debian.org:80 --recv 15CDDA6AE19135A2
# Download specific release and it's signing file
RUN wget http://thekelleys.org.uk/dnsmasq/dnsmasq-$VERSION.tar.gz
RUN wget http://thekelleys.org.uk/dnsmasq/dnsmasq-$VERSION.tar.gz.asc
# Verify downloaded file with signing key and extract only if verification passes
RUN gpg --verify dnsmasq-$VERSION.tar.gz.asc dnsmasq-$VERSION.tar.gz && tar -xzf dnsmasq-$VERSION.tar.gz
# Use WORKDIR instead of cd inside dockerfile for clarity and reliability
WORKDIR /dnsmasq-$VERSION
# Compile binary to copy in next image
RUN make install

# Pinning to latest as of 2021/09/29
FROM gcr.io/distroless/base-debian10@sha256:aff0b0d6766cce25bd47bacb3ed67ae866952585c0735ff3bdb70fdfeac8992a 
# Do not use maintainer command, it's deprecated
LABEL maintainer="horihiro"

USER root

COPY --from=build /usr/local/sbin/dnsmasq /usr/local/sbin/dnsmasq
COPY dnsmasq.conf /etc/dnsmasq.conf

EXPOSE 53 53/udp
ENTRYPOINT ["dnsmasq", "--no-daemon"]
