FROM ubuntu:16.04
MAINTAINER Robert F. Dickerson <rfdickerson@gmail.com>
LABEL description="Builds Swift projects on Linux"

ENV HOME /root
ENV WORK_DIR /root

WORKDIR /root

RUN apt-get update && apt-get install -y \
  clang \
  git \
  libicu-dev \
  wget \
  libcurl4-openssl-dev \
  libssl-dev \
  libxml2-dev

RUN wget https://swift.org/builds/swift-3.1-release/ubuntu1604/swift-3.1-RELEASE/swift-3.1-RELEASE-ubuntu16.04.tar.gz
RUN tar xzvf swift-3.1-RELEASE-ubuntu16.04.tar.gz -C /root
ENV PATH /root/swift-3.1-RELEASE-ubuntu16.04/usr/bin:$PATH

EXPOSE 8080
EXPOSE 1234

COPY /build-swift-project.sh /
ENTRYPOINT ["bash", "/build-swift-project.sh"]

