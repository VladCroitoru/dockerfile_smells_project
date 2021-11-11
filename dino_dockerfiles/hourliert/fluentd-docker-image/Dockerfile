FROM ubuntu:14.04
MAINTAINER TAGOMORI Satoshi <tagomoris@gmail.com>
LABEL Description="Fluentd docker image" Vendor="Fluent Organization" Version="1.0"

RUN apt-get update -y && apt-get install -y \
              autoconf \
              bison \
              build-essential \
              curl \      
              git \
              libffi-dev \              
              libgdbm3 \
              libgdbm-dev \
              libncurses5-dev \
              libreadline6-dev \              
              libssl-dev \
              libyaml-dev \
              zlib1g-dev \              
        && rm -rf /var/lib/apt/lists/*

RUN groupadd fluentd -g 2422
RUN useradd fluentd -d /home/fluentd -m -u 2422 -g 2422
RUN chown -R fluentd:fluentd /home/fluentd

# for log storage (maybe shared with host)
RUN mkdir -p /fluentd/log
# configuration/plugins path (default: copied from .)
RUN mkdir -p /fluentd/etc
RUN mkdir -p /fluentd/plugins

RUN chown -R fluentd:fluentd /fluentd

USER fluentd
WORKDIR /home/fluentd

RUN git clone https://github.com/tagomoris/xbuild.git /home/fluentd/.xbuild
RUN /home/fluentd/.xbuild/ruby-install 2.2.2 /home/fluentd/ruby

ENV PATH /home/fluentd/ruby/bin:$PATH
RUN gem install fluentd -v 0.12.15

# RUN gem install fluent-plugin-webhdfs

COPY fluent.conf /fluentd/etc/
ONBUILD COPY fluent.conf /fluentd/etc/
ONBUILD COPY plugins/* /fluentd/plugins/

WORKDIR /home/fluentd

ENV FLUENTD_OPT=""
ENV FLUENTD_CONF="fluent.conf"

EXPOSE 24224

### docker run -p 24224 -v `pwd`/log: -v `pwd`/log:/home/ubuntu/log fluent/fluentd:latest
CMD fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
