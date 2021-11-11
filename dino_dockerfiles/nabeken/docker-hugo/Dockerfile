FROM ubuntu:14.04
MAINTAINER TANABE Ken-ichi <nabeken@tknetworks.org>

ENV GOPATH /usr/local
ENV PATH /usr/local/go/bin:$PATH

# ENV HUGO_RELEASE https://github.com/spf13/hugo/releases/download/v0.12/hugo_0.12_linux_amd64.tar.gz

EXPOSE 1313

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y \
  curl \
  git \
  mercurial \
  && :

# RUN curl -L $HUGO_RELEASE > /tmp/hugo.tar.gz
# RUN tar -C /tmp -zxf /tmp/hugo.tar.gz && \
#   mv /tmp/hugo_* /tmp/hugo && \
#   mv /tmp/hugo/hugo_* /usr/local/bin/hugo

RUN curl -L https://storage.googleapis.com/golang/go1.3.3.linux-amd64.tar.gz | tar -C /usr/local -zxf -
RUN /usr/local/go/bin/go get -v github.com/spf13/hugo

ENTRYPOINT ["hugo"]
