FROM brucepc/symfony-base:7.1-fpm

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && apt-get update -yqq \
    && apt-get install -y apt-transport-https lsb-release > /dev/null 2>&1 \
    && rm -rf /var/lib/apt/lists/* \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list 

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get install -y nodejs yarn \
    && rm -rf /var/lib/apt/lists/*
