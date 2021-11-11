FROM alpine:latest

RUN apk add --no-cache \
         curl \
         bash \
         jq \
         git \
         netcat-openbsd \
         ruby \
         ruby-dev \
         ruby-bundler \
         ruby-json \
         ruby-rdoc \
         ruby-irb \
         openssh-client \
         expect \
         python2 \
         python2-dev \
         python3 \
         python3-dev \
         py2-pip \
         mariadb-dev \
         build-base \
         rsync \
         mysql-client \
         postgresql-client \
         openssl \
         openjdk8-jre \
         bc \
    && curl -L -o /usr/local/bin/listcompute https://github.com/arwineap/listcompute/releases/download/v1.1/listcompute_musl_amd64 \
    && chmod +x /usr/local/bin/listcompute \
    && pip3 install awscli boto3 pandas \
    && gem install capistrano -v 3.6.1 \
    && curl -o /root/terraform.zip https://releases.hashicorp.com/terraform/0.11.8/terraform_0.11.8_linux_amd64.zip \
    && unzip -d /usr/local/bin /root/terraform.zip \
    && rm -f /root/terraform.zip
