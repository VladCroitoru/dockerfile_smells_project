FROM ubuntu:16.04
MAINTAINER "James Oguya <oguyajames@gmail.com>"

# install wget
RUN apt-get update; apt-get install -yy --no-install-recommends wget

# download & install hugo
ENV HUGO_VERSION 0.19
RUN wget --no-check-certificate -qO- https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz | tar xzv
RUN cp hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64 /bin/hugo

# blog dir.
RUN mkdir /blog
WORKDIR /blog

# automatically build blog
ADD . /blog
RUN hugo -d /blog

# expose default hugo port
EXPOSE 1313

# By default, serve site
ENV HUGO_BASE_URL http://localhost:1313
CMD hugo server -b ${HUGO_BASE_URL} --bind=0.0.0.0
