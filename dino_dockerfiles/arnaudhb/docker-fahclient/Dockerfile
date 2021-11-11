FROM ubuntu:20.04

# non interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# build args
ARG BRAND
ARG VERSION

# install packages needed by fahclient installer
RUN apt-get update && apt-get install -y bzip2

# add files to image
COPY docker-entrypoint.sh /
COPY add/config.xml /etc/fahclient/
ADD https://download.foldingathome.org/releases/public/release/fahclient/debian-stable-64bit/${BRAND}/fahclient_${VERSION}_amd64.deb /fahclient.deb

# do not properly install package, but only retrieve binaries
RUN dpkg -x ./fahclient.deb ./deb &&\
 mv deb/usr/bin/* /usr/bin &&\
 rm -rf *.deb &&\
 rm -rf deb &&\
 chmod u+x /docker-entrypoint.sh &&\
 rm -rf /var/lib/apt/lists/*

# go to homedir
WORKDIR /var/lib/fahclient

# entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]
