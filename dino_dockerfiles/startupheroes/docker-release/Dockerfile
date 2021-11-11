FROM openjdk:16-jdk-slim

RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf

RUN apt-get update && \
    apt-get install -y curl \
                       apt-transport-https \
                       ca-certificates \
                       gnupg-agent \
                       software-properties-common \
                       git \
                       nodejs \
                       npm \
                       coreutils \
                       python3 \
                       python3-pip \
                       groff \
                       jpegoptim \
		       libjpeg-dev \
		       build-essential \
                       tzdata \
                       imagemagick \
                       ttf-dejavu \
                       gettext && \
    pip3 install --upgrade awscli==1.18.51  && \
    cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    echo "Europe/Moscow" > /etc/timezone

RUN  mkdir -p /opt/ortools && curl -sL https://github.com/google/or-tools/releases/download/v7.5/or-tools_debian-10_v7.5.7466.tar.gz | tar xvz -C /opt/ortools/ --strip-components=1
