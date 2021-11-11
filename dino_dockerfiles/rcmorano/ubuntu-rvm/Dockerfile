FROM ubuntu:xenial
MAINTAINER rcmova@gmail.com
RUN apt-get update
RUN apt-get install -yo 'APT::Install-Recommends=false' -o 'APT::Install-Suggests=false' curl ca-certificates
RUN curl -sSL http://get.rvm.io | bash -s stable --ruby

CMD ["/bin/bash","--login"]
