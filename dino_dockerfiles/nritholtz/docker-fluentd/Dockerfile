FROM inzinger/alpine-ruby:2.2.2
MAINTAINER Nathaniel Ritholtz <nritholtz@gmail.com>

# Install required packages
RUN apk add --update \
              build-base \
              ruby-dev \
              bash \
              curl \      
              supervisor \           
  && rm -rf /var/cache/apk/*

# Install Fluentd
RUN gem install fluentd -v 0.12.16 --no-rdoc --no-ri && \
  fluent-gem install fluent-plugin-cloudwatch-logs -v 0.1.2 

# Install docker-gen
RUN wget https://github.com/jwilder/docker-gen/releases/download/0.4.2/docker-gen-linux-amd64-0.4.2.tar.gz \
 && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-0.4.2.tar.gz \
 && rm docker-gen-linux-amd64-0.4.2.tar.gz

# Copy fluentd config file
COPY fluent.conf /etc/fluent/

ADD . /

EXPOSE 24224

CMD ["/bin/bash", "./bootstrap.sh"]