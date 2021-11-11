FROM ruby:2.4.0

ENV RUBYOPT -EUTF-8

RUN apt-get update

# Node.js
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \
    && apt-get install -y nodejs

# yarn
#RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -\
#    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
#    && apt-get update \
#    && apt-get install -y yarn=0.24.6

RUN npm install -g yarn@0.24.6

RUN apt-get install build-essential chrpath libssl-dev libxft-dev -y \
    && apt-get install libfreetype6 libfreetype6-dev -y \
    && apt-get install libfontconfig1 libfontconfig1-dev -y \
    && export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" \
    && curl -L -O https://github.com/Medium/phantomjs/releases/download/v2.1.1/$PHANTOM_JS.tar.bz2 \
    && tar xvjf $PHANTOM_JS.tar.bz2 \
    && mv $PHANTOM_JS /usr/local/share \
    && ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin \
    && phantomjs --version

# Install Java
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > /etc/apt/sources.list.d/webupd8team-java-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
RUN apt-get update \
    && apt-get install -y --no-install-recommends oracle-java8-installer \
    && apt-get clean all

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Install Elasticsearch
RUN curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.4.3.tar.gz \
    && tar -xvf elasticsearch-5.4.3.tar.gz \
    && elasticsearch-5.4.3/bin/elasticsearch-plugin install analysis-kuromoji \
    && elasticsearch-5.4.3/bin/elasticsearch-plugin install analysis-icu

RUN rm -rf /var/lib/apt/lists/*

RUN npm install -g n \
    && n 7.8.0 \
    && node -v \
    && npm -v

RUN useradd circleci-test
USER circleci-test
