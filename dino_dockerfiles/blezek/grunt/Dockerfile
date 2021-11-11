# Build a CentOS based system

# Use CentOS 7, but could be any Linux
FROM centos:7

MAINTAINER "Daniel Blezek" blezek.daniel@mayo.edu

# Create a user and do everything as that user
VOLUME /data

# Build grunt
RUN yum install -y git wget curl
RUN cd /root && wget --quiet https://storage.googleapis.com/golang/go1.7.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf /root/go1.7.linux-amd64.tar.gz
RUN rm -f /root/go1.7.linux-amd64.tar.gz
ENV GOPATH=/root
ENV PATH=/usr/local/go/bin:${PATH}

# Copy local files into GOPATH
ADD .  $GOPATH/src/github.com/Mayo-QIN/grunt/
RUN go install github.com/Mayo-QIN/grunt

# Install files
RUN mkdir -p /grunt.d
RUN cp /root/bin/grunt /bin/grunt
COPY gruntfile.yml /gruntfile.yml

# Start grunt in /data with the given gruntfile
WORKDIR /data
CMD ["/bin/grunt", "/gruntfile.yml"]

# We expose port 9901 by default
EXPOSE 9901:9901
