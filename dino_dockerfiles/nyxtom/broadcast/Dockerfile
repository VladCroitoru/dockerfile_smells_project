FROM google/debian:wheezy

RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl build-essential ca-certificates git mercurial bzr

# Install Go 1.3.2
RUN curl -s https://storage.googleapis.com/golang/go1.3.2.linux-amd64.tar.gz | tar -v -C /usr/local -xz
ENV GOPATH /go
ENV GOROOT /usr/local/go
ENV PATH /usr/local/go/bin:/go/bin:/usr/local/bin:$PATH

# Install confd
RUN curl -L https://github.com/kelseyhightower/confd/releases/download/v0.3.0/confd_0.3.0_linux_amd64.tar.gz | tar xz
RUN mv confd /usr/local/bin/confd

# Create directories
RUN mkdir -p /etc/confd/conf.d

# Install broadcast
RUN mkdir -p /go/src/github.com/nyxtom/broadcast
WORKDIR /go/src/github.com/nyxtom
RUN git clone https://github.com/nyxtom/broadcast.git
WORKDIR /go/src/github.com/nyxtom/broadcast
ADD . /go/src/github.com/nyxtom/broadcast

# Add confd files
ADD ./etc/broadcast.conf /etc/confd/conf.d/broadcast.conf

# Run make to install
RUN make

# Define mountable directories
VOLUME ["/data"]

# Working directory
WORKDIR /data

# Define default command
CMD ["$GOPATH/bin/broadcast-server", "-config=/etc/confd/conf.d/broadcast.conf"]

# Expose port
EXPOSE 7331
