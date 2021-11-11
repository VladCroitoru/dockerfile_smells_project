FROM ruby:2.2-onbuild

RUN apt-get update && \
    apt-get install -y \
        curl \
        git \
        && \
    curl https://deb.nodesource.com/setup_4.x | bash - && \
    apt-get install -y nodejs && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN npm install
