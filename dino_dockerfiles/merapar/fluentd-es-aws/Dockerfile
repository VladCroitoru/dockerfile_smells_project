FROM ubuntu:16.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
 && apt-get install -y curl ruby2.3 ruby2.3-dev make g++ \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*


RUN gem install fluentd:0.14.21 \
 && gem install fluent-plugin-kubernetes_metadata_filter:0.29.0 \
   fluent-plugin-flatten-hash:0.5.0 \
   fluent-plugin-systemd:0.3.0 \
   fluent-plugin-aws-elasticsearch-service:0.1.6 \
   && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem
