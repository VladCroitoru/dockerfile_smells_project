FROM ubuntu:14.04
MAINTAINER github/metalivedev
RUN apt-get update && apt-get install -y build-essential libssl-dev openssl ca-certificates
ADD . /opt/siege-src
WORKDIR /opt/siege-src
RUN ./configure --with-ssl=/usr
RUN make install
# Default directory for logs
RUN mkdir -p /usr/local/var
ENTRYPOINT ["/usr/local/bin/siege"]
