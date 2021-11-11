# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.10
MAINTAINER Jann Kleen <jann.kleen@freshx.de>

# Set correct environment variables.
ENV HOME /root

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update
RUN apt-get -y install ca-certificates build-essential git
RUN curl https://storage.googleapis.com/golang/go1.2.2.linux-amd64.tar.gz > /usr/local/golang.tgz
RUN tar -C /usr/local -xzf /usr/local/golang.tgz
ENV PATH  /usr/local/go/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin
ENV GOPATH  /go
ENV GOROOT  /usr/local/go
RUN go get github.com/JannKleen/sendgrid-statsd
WORKDIR /go/src/github.com/JannKleen/sendgrid-statsd
ADD . /go/src/github.com/JannKleen/sendgrid-statsd
RUN go get
RUN go build
EXPOSE 9090
ENTRYPOINT ./start_sendgrid_statsd.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
