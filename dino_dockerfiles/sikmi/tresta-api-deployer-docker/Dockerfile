FROM sikmi/awseb-deployer-docker

# ruby install
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.5/ruby-2.5.1.tar.gz && \
    tar -zxvf ruby-2.5.1.tar.gz && \
    cd ruby-2.5.1 && \
    ./configure --disable-install-doc && \
    make && \
    make install && \
    cd .. && \
    rm -r ruby-2.5.1 ruby-2.5.1.tar.gz

# node install
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install nodejs

# yarn install
RUN mkdir -p /var/lib/apt/lists \
    && apt-get update \
    && apt-get install -y apt-transport-https git --no-install-recommends \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get -y install yarn \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN gem install bundler
# firebase install
RUN npm install -g firebase-tools
