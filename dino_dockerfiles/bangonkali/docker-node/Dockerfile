FROM phusion/baseimage:0.9.22

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Use bash instead.
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Download and install node
RUN apt-get install -y software-properties-common \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && node -v \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install -y yarn

# Download and install logstash
RUN curl -sS https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
    && apt-get update && apt-get install -y apt-transport-https default-jre default-jdk \
    && echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-5.x.list \
    && apt-get update && apt-get install -y logstash \
    && /usr/share/logstash/bin/logstash-plugin install logstash-output-loggly

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
